from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import cloudinary
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = 'NEUXBAYXV&^LAKX$LXNA*MIWHSA^JAQWXC*PZX&'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("@Admin123")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 4

db = SQLAlchemy(app)

cloudinary.config(cloud_name='dbitlfhjx',
                  api_key='889556431667884',
                  api_secret='ycTIF7ajW7_lKzO_Ff4zAwpeB6g')

login = LoginManager(app)