from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anish123!'
app.config['MYSQL_DB'] = 'world'

mysql = MySQL(app)

from sqlalchemy import create_engine
sqlEngine = create_engine('mysql+pymysql://root:Anish123!@localhost/world')


from ResortApp import main
from ResortApp import guest
from ResortApp import data_analysis
from ResortApp import user
