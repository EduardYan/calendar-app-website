"""
This file have some
configurations and initials values
for the server.

For execute the server, execute
the file index.py

"""

from flask import Flask
from routes.calendar_routes import calendar

# creating
app = Flask(__name__)


# getting routes
app.register_blueprint(calendar)