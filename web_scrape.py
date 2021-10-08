from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
import time

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

chrome_options = Options()
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())

def getdineLA():
	db.execute("DELETE FROM dinela")	
	driver.get("https://www.discoverlosangeles.com/dinela")

	#Scroll to bottom of page in order to load all of the content
	no_of_scrolls = 10
	while no_of_scrolls:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
		no_of_scrolls -=1		

	content = driver.page_source
	soup = BeautifulSoup(content, "html.parser")
	for a in soup.find_all("table", attrs={"class": "views-table views-view-table cols-7 sticky-enabled sticky-table"}):
		body = a.find("tbody")
		for b in body.find_all("tr"):
			#Extract name of restaurant
			#Extract link to restaurant

	#db.commit()


def getYelp():
	db.execute("DELETE FROM yelp")	

def main():
	getdineLA()
	getYelp()

if __name__ == '__main__':
	main()
