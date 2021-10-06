import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DineLA(db.Model):
	__tablename__ = "dinela"
	id = db.Column(db.Integer, primary_key = True)

class Yelp(db.Model):
	__tablename__ = "yelp"
	id = db.Column(db.Integer, primary_key = True)
