"""
This file have the model
for the visits in the database.
"""

from utils.db import db

class NumberValueInvalid(TypeError):
  """
  Class for create execption
  in case the number passed for parameter not is valid.
  """
  pass


class Visists(db.Model):
  """
  Model for the visits:

  number:str The number for the visit created

  """

  # creating columns
  number = db.Column(db.Integer, primary_key = True)

  def __init__(self, number:int) -> None:
    if type(number) not in [int]:
      raise NumberValueInvalid('The value for the database is invalid')

    # values
    self.number = number