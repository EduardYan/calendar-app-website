"""
This file have
the routes to visit for the website.
"""

from flask import Blueprint, render_template
from utils.db import db
from models.visits import Visists
from utils.counter import get_counter

# routes
calendar = Blueprint('calendar', __name__)

# counter for the visits
counter = get_counter()


def add_visit(counter:int):
  """
  Add the visit passed for parameter
  """

  visits = Visists.query.all()
  visit = Visists(int(counter))
  db.session.add(visit)
  db.session.commit()


@calendar.route('/')
@calendar.route('/home')
def home():
  """
  Initial route for the server.
  """

  global counter
  add_visit(counter)
  counter += 1 # adding the visits
  return render_template('index.html')

@calendar.route('/download')
def get_download():
  """
  Route for render the page of download.
  """

  global counter
  add_visit(counter) # adding visit
  counter += 1

  return render_template('get-download.html')