# ProgettoCineTicket

CineTicket is a website that deals with cinema, allows users to register and log in. Users who have an account have the option to receive a promotion to redeem once they arrive at the cinema.




COMPONENTS USED:

1. Python3
2. Flask
3. SQL lite
4. HTML
5. Javascript
6. CSS



INSTALLATION OF PROJECT COMPONENTS:

pip3 install -r requirements.txt



DATABASE CONFIGURATION WITH SQLITE AND SQL_ALCHEMY:

After writing the classes (even the user class) of the database on python we can proceed with the configuration of the database and the creation inside the folder path of our project.

1. select the project folder path via the "cd" command
2. write in the terminal "python3" to use python
3. write in the terminal "from app import db"
4. write in the terminal "db.create_all()"
5. write in the terminal "exit()"



SQL LITE MENU VIA TERMINAL:

1. select the project folder path via the "cd" command
2. write in the terminal "sqlite3 database.db" and press enter
3. write in the terminal ".tables" to view all the tables of the database
4. write in the terminal ".exit()" to leave



START SERVER:

1. select the project folder path via the "cd" command
2. python3 app.py ----> ON MAC     OR     python app.py ----> ON WINDOWS

the server will start from port 8000 previously chosen via python

Now everything is ready, you can have fun on our website!
