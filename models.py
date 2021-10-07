import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DineLA(db.Model):
	__tablename__ = "dinela"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Integer, nullable=False)
	neighborhood = db.Column(db.Integer, nullable=False)
	lunchPrice = db.Column(db.Integer, nullable=True)
	dinnerPrice = db.Column(db.Integer, nullable=True)


class Yelp(db.Model):
	__tablename__ = "yelp"
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Integer, nullable=False)
	rating = db.Column(db.Integer, nullable=False)
