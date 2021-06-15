from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy

import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '77c8325cef3a37923db388c1'
db = SQLAlchemy(app)

from market import routes