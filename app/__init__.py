from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
	SECRET_KEY = '',
	SQLALCHEMY_DATABASE_URI = '' + os.path.join(basdir, 'app.db')
)

db = SQLAlchemy(myaoo_obj)

from app import routes, models, forms
