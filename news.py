import requests
from bs4 import BeautifulSoup
#target page url
URL = "https://www.bbc.com"
#connects with the target url and getting it
page = requests.get(URL)

#change the page format into html
soup = BeautifulSoup(page.content, "html.parser")

news = soup.find_all("li", class_="media-list__item")


