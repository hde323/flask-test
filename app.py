from flask import Flask , render_template , redirect , request
import requests
from bs4 import BeautifulSoup
from news import news
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", news = news)

if __name__ == "__main__":
    app.run(debug=True)
