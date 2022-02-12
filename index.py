"""
Principal file
for execute the server.
"""

from app import app
from utils.db import db

# creating tables
with app.app_context():
  db.create_all()

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug = False)