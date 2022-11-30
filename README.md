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

```
pip3 install -r requirements.txt
```

## DATABASE CONFIGURATION WITH SQLITE AND SQL_ALCHEMY:

After writing the classes (even the user class) of the database on python we can proceed with the configuration of the database and the creation inside the folder path of our project.

- select the project folder path via the ```cd``` command
- write in the terminal ```python3``` to use python
- write in the terminal ```from app import db```
- write in the terminal ```db.create_all()```
- write in the terminal ```exit()```


## SQL LITE MENU VIA TERMINAL:

- select the project folder path via the ```cd``` command
- write in the terminal ```sqlite3 database.db``` and press enter
- write in the terminal ```.tables``` to view all the tables of the database
- write in the terminal ```.exit()``` to leave


## START SERVER:

- select the project folder path via the ```cd``` command
- ```python3 app.py``` ----> ON MAC OR ```python app.py``` ----> ON WINDOWS

the server will start from port 8000 previously chosen via python

# Now everything is ready, you can have fun on our website!