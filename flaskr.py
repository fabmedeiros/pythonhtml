import sqlite3
from flask import Flask

# config
DATABASE = './flaskr.db'
SECRET_KEY = 'pudim'
USERNAME = 'admin'
PASSWORD = 'admin'

# aplicacao
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'