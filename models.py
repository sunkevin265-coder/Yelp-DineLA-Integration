import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DineLA(db.Model):
	__tablename__ = "dinela"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	neighborhood = db.Column(db.String, nullable=False)
	lunchPrice = db.Column(db.String, nullable=True)
	dinnerPrice = db.Column(db.String, nullable=True)
	linkToDineLA = db.Column(db.String, nullable=False)
	cuisine = db.Column(db.String, nullable=False)

class Yelp(db.Model):
	__tablename__ = "yelp"
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, nullable=False)
	rating = db.Column(db.String, nullable=False)
