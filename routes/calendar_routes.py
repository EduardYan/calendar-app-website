"""
This file have
the routes to visit for the website.
"""

from flask import Blueprint, render_template


calendar = Blueprint('calendar', __name__)

@calendar.route('/')
@calendar.route('/home')
def home():
  """
  Initial route for the server.
  """

  return render_template('index.html')

@calendar.route('/download')
def get_download():
  """
  Route for render the page of download.
  """

  return render_template('get-download.html')