import sqlite3

from flask import Flask, render_template, url_for, redirect, flash, session, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, Regexp, EqualTo
from flask_bcrypt import Bcrypt

import os
import pathlib
import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests


app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'A8a9a9s0'

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "352938198983-bvvbamujntvrfn4iqilae9fadrqdino0.apps.googleusercontent.com"
client_secret_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
  client_secrets_file=client_secret_file,
  scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
  redirect_uri="http://localhost:8000/callback"
)


def connection_db():
  connection = sqlite3.connect('database.db')
  connection.row_factory = sqlite3.Row
  return connection


@app.route("/login_google")
def login_google():
  authorization_url, state = flow.authorization_url()
  session["state"] = state
  return redirect(authorization_url)


@app.route("/callback")
def callback():
  flow.fetch_token(authorization_response=request.url)

  if not session["state"] == request.args["state"]:
    abort(500)  # State does not match!

  credentials = flow.credentials
  request_session = requests.session()
  cached_session = cachecontrol.CacheControl(request_session)
  token_request = google.auth.transport.requests.Request(session=cached_session)

  id_info = id_token.verify_oauth2_token(
    id_token=credentials._id_token,
    request=token_request,
    audience=GOOGLE_CLIENT_ID
  )
  session["google_id"] = id_info.get("sub")
  session["username"] = id_info.get("name")
  session['name'] = id_info.get('given_name')
  session['last_name'] = id_info.get('family_name')
  session['email'] = id_info.get("email")
  session['photo'] = id_info.get("picture")
  connection = connection_db()
  cur_sql = connection.cursor()
  res = cur_sql.execute('SELECT email FROM User where email=?', [session['email']], )
  if res.fetchone():
    return redirect("/")
  else:
    connection.execute('INSERT INTO User (username, name, surname, email) VALUES (?,?,?,?)', (session['username'], session['name'], session['last_name'], session['email']))
    connection.commit()
    connection.close()
    return redirect("/")


@app.route("/logout_google")
def logout_google():
  session.clear()
  return redirect("/")


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), nullable=False)
  name = db.Column(db.String(50), nullable=False)
  surname = db.Column(db.String(50), nullable=False)
  cellular = db.Column(db.String(50), nullable=True, unique=True)
  address = db.Column(db.String(50), nullable=True)
  city = db.Column(db.String(50), nullable=True)
  state = db.Column(db.String(50), nullable=True)
  email = db.Column(db.String(50), nullable=True)
  password = db.Column(db.String(50))


class SignupForm(FlaskForm):
  name = StringField(validators=[InputRequired(), Length(min=3, max=50), Regexp("^[A-Za-z]*$", 0, "name must contain only characters")], render_kw={"placeholder": "Enter your name"})
  surname = StringField(validators=[InputRequired(), Length(min=3, max=50), Regexp("^[A-Za-z]*$", 0, "surname must contain only characters")], render_kw={"placeholder": "Enter your surname"})
  username = StringField(validators=[InputRequired(), Length(min=6, max=50, message="Username must contain at least 6 characters"), Regexp("^[A-Za-z][A-Za-z0-9_.]*$", 0, "Username must contain characters, numbers...")], render_kw={"placeholder": "Enter your username"})
  cellular = StringField(validators=[InputRequired(), Length(min=10, max=10), Regexp("^[-+]?[0-9]+$", 0, "Mobile number can contain only numbers")], render_kw={"placeholder": "Enter your mobile number"})
  address = StringField(validators=[InputRequired(), Length(min=3, max=50)], render_kw={"placeholder": "Enter your address"})
  city = StringField(validators=[InputRequired(), Length(min=1, max=50)], render_kw={"placeholder": "Enter your city"})
  state = StringField(validators=[InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Enter your state"})
  email = StringField(validators=[InputRequired(), Length(min=10, max=150), Regexp("[^@]+@[^@]+\.[^@]+", 0, "email is not valid")], render_kw={"placeholder": "Enter your email"})
  password = PasswordField(validators=[InputRequired(), Length(min=6, max=20)], render_kw={"placeholder": "Enter your password"})
  c_password = PasswordField(validators=[InputRequired(), Length(min=6, max=20), EqualTo("password", message="Passwords do not match")], render_kw={"placeholder": "Confirm your password"})
  submit = SubmitField("SIGN UP")

  def validate_email(self, email):
    existing_user_email = User.query.filter_by(email=email.data).first()
    if existing_user_email:
      raise ValidationError('That email already exists. Please choose a different one.')

  def validate_username(self, username):
    existing_username = User.query.filter_by(username=username.data).first()
    if existing_username:
      raise ValidationError('That username already exists. Please choose a different one.')

  def validate_cellular(self, cellular):
    existing_cellular = User.query.filter_by(cellular=cellular.data).first()
    if existing_cellular:
      raise ValidationError('That phone number already exists. Please choose a different one.')


class LoginForm(FlaskForm):
  email = StringField(validators=[InputRequired(), Length(min=10, max=150)], render_kw={"placeholder": "Enter your email"})
  password = PasswordField(validators=[InputRequired(), Length(min=6, max=20)], render_kw={"placeholder": "Enter your password"})
  submit = SubmitField('SIGN IN')


@app.route('/blackpanther')
def blackpanther():
  return render_template('BlackPantherPage.html')


@app.route('/blackadam')
def blackadam():
  return render_template('BlackAdamPage.html')


@app.route('/uncharted')
def uncharted():
  return render_template('UnchartedPage.html')


@app.route('/harrypotter')
def harrypotter():
  return render_template('HarrypotterPage.html')


@app.route('/promotion')
def promotion():
    return render_template('Promotion.html')


@app.route('/home')
def home():
    return render_template('Index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  msg = ""

  if current_user.is_authenticated:
    return redirect(url_for('home'))

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user:
      if bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user)
        return redirect(url_for('home'))
      else:
        msg = "Your email or password aren't correct"
    else:
      msg = "Your email or password aren't correct"

  return render_template('Login.html', form=form, msg=msg)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
  logout_user()
  return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  msg = ""

  if form.validate_on_submit():
    try:
     hashed_password = bcrypt.generate_password_hash(form.password.data)
     new_user = User(name=form.name.data, surname=form.surname.data, username=form.username.data, cellular=form.cellular.data, address=form.address.data, city=form.city.data, state=form.state.data, email=form.email.data, password=hashed_password)
     db.session.add(new_user)
     db.session.commit()
     flash(f"Successfully", "success")
     return redirect(url_for('login'))

    except Exception as excep:
      flash(excep, "danger")

  return render_template('SignUp.html', form=form, msg=msg)


@app.route('/')
def homepage():
  return redirect(url_for('home'))


@app.route('/contacts')
def contacts():
  return render_template('Contacts.html')


if __name__ == '__main__':
  app.run(debug=True, host="localhost", port=8000)
