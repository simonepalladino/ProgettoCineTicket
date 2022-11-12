from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, Regexp, EqualTo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), nullable=False, unique=True)
  name = db.Column(db.String(50), nullable = False)
  surname = db.Column(db.String(50), nullable=False)
  cellular = db.Column(db.String(50), nullable=True, unique=True)
  address = db.Column(db.String(50), nullable= True)
  city = db.Column(db.String(50), nullable = True)
  state = db.Column(db.String(50),nullable = True)
  email = db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(50), nullable=False)


class RegisterForm (FlaskForm):
  name = StringField(validators = [InputRequired(), Length(min=3, max=50), Regexp("^[A-Za-z]*$",0,"name must contain only characters")], render_kw={"placeholder":"Enter your name"})
  surname = StringField(validators = [InputRequired(), Length(min=3, max=50), Regexp("^[A-Za-z]*$",0,"surname must contain only characters")], render_kw={"placeholder":"Enter your surname"})
  username = StringField(validators = [InputRequired(), Length(min=6, max=50, message="Username must contain at least 6 characters"), Regexp("^[A-Za-z][A-Za-z0-9_.]*$",0,"Username must contain characters, numbers...")], render_kw={"placeholder": "Enter your username"})
  cellular = StringField(validators = [InputRequired(), Length(min=10, max=10), Regexp("^[-+]?[0-9]+$",0,"Mobile number can contain only numbers")], render_kw={"placeholder": "Enter your mobile number"})
  address = StringField(validators= [InputRequired(), Length(min=5, max= 50)], render_kw={"placeholder":"Enter your address"})
  city= StringField(validators=[InputRequired(), Length(min=5, max=50)], render_kw={"placeholder":"Enter your city"})
  state = StringField(validators=[InputRequired(), Length(min=5, max=50)], render_kw={"placeholder":"Enter your state"})
  email = StringField(validators = [InputRequired(), Length(min=10, max=150), Regexp("[^@]+@[^@]+\.[^@]+",0,"email is not valid")], render_kw={"placeholder":"Please enter your email"})
  password = PasswordField(validators = [InputRequired(), Length(min=6,max=20)], render_kw={"placeholder":"Please enter your password"})
  confirm_password = PasswordField(validators = [InputRequired(), Length(min=6,max=20), EqualTo("password", message = "Passwords do not match")], render_kw={"placeholder":"Confirm your passwprd"})
  submit = SubmitField('Sign in')


class LoginForm (FlaskForm):
  email = StringField(validators = [InputRequired(), Length(min=10, max=150)], render_kw={"placeholder":"Enter your email"})
  password = PasswordField(validators = [InputRequired(), Length(min=6,max=20)], render_kw={"placeholder":"Enter your password"})
  submit = SubmitField('Login')


def validate_email(self, email):
  existing_user_email = User.query.filter_by(email=email.data).first()
  if existing_user_email:
    raise ValidationError('That email already exists. Please choose a different one.')


@app.route('/home')
def home():
  if current_user.is_authenticated:
    return render_template('Index.html')
  else:
    return render_template('Indexanonymous.html')

@app.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  msg=""

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user:
      if bcrypt.check_password_hash(user.password, form.password.data):
         login_user(user)
         return redirect(url_for('home'))
      else:
        msg = "Email or password not valid"
    else:
      msg = "Email or password not valid"

  return render_template('Login.html', form=form, msg=msg)


@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
  logout_user()
  return redirect(url_for('home'))

@app.route('/register',methods=['GET','POST'])
def register():
  form = RegisterForm()
  msg = ""

  if form.validate_on_submit():
    try:
      hashed_password = bcrypt.generate_password_hash(form.password.data)
      new_user = User(name=form.name.data, surname=form.surname.data, username=form.username.data, cellular=form.cellular.data, address=form.address.data, city=form.city.data, state=form.state.data,email=form.email.data, password=hashed_password)
      db.session.add(new_user)
      db.session.commit()
      flash(f"Successfully","success")
      return redirect(url_for('login'))


    except Exception as excep:
      flash(excep,"danger")

  return render_template('SignUp.html', form=form, msg=msg)

if __name__ == '__main__':
  app.run(debug=True)




