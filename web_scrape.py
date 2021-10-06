from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def getdineLA():
	db.execute("DELETE FROM active")	

def getYelp():
	return

def main():
	getdineLA()
	getYelp()
