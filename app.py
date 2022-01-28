"""
This file have some
configurations and initials values
for the server.

For execute the server, execute
the file index.py

"""

from flask import Flask
from routes.calendar_routes import calendar
from flask_sqlalchemy import SQLAlchemy
from config import SQLITE_CONNECTION

# creating
app = Flask(__name__)

# settins
app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database
SQLAlchemy(app)

# getting routes
app.register_blueprint(calendar)