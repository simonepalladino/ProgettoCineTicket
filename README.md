# CineTicket is a website that deals with cinema, allows users to register and log in. Users who have an account have the option to receive a promotion to redeem once they arrive at the cinema.

## COMPONENTS USED:

- Python3
- Flask
- SQL lite
- HTML
- Javascript
- CSS


## INSTALLATION OF PROJECT COMPONENTS:

select the project folder path via the ```cd``` command

Now write in the terminal:
```
pip3 install -r requirements.txt
```

## GOOGLE CLOUD PLATFORM CONFIGURATION:

1. create a google cloud platform account or login with your google account on console.cloud.google.com
2. Go to dashboard and create a new project
3. open the project
4. Go to API & Services ---> Credentials
5. Configure consent screen
Settings consent screen:
-User Type: External
-Set the name and the other information
6. Create credentials ---> Oauth client ID
7. Set the name and the other information of the app and choose Web application as Application type
8. Download client_secret.json file


## DATABASE CONFIGURATION WITH SQLITE AND SQL_ALCHEMY:

After writing the classes (even the user class) of the database on python we can proceed with the configuration of the database and the creation inside the folder path of our project.

1. select the project folder path via the ```cd``` command
2. write in the terminal ```python3``` to use python
3. write in the terminal ```from app import db```
4. write in the terminal ```db.create_all()```
5. write in the terminal ```exit()```


## SQL LITE MENU VIA TERMINAL:

1. select the project folder path via the ```cd``` command
2. write in the terminal ```sqlite3 database.db``` and press enter
3. write in the terminal ```.tables``` to view all the tables of the database
4. write in the terminal ```.exit()``` to leave


## START SERVER:

1. select the project folder path via the ```cd``` command
2. write in the terminal:
ON MAC
```python3 app.py```
ON WINDOWS
```python app.py```

the server will start from port 8000 previously chosen via python

# Now everything is ready, you can have fun on our website!
