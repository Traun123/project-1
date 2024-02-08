# Scraper

This is some python code that is capable of crawling and scraping dynamic Web sites.

**Dynamic Web sites** are sites that:
 - dynamically load content (e.g. gets search results from an AJAX call)
 - render their HTML using javascript (e.g. any reactjs Web site)

Scraper is able to scrape dynamic Web sites by loading the page in a virtual Webkit browser, allowing the JavaScript to run, before parsing the HTML.
important library
from base64 import urlsafe_b64decode
import requests
from bs4 import BeautifulSoup
url="https://www.python.org/"
scrapping letest_articles
from base64 import urlsafe_b64decode
import requests
from bs4 import BeautifulSoup

def get_letest_python_articles():
    url="https://www.python.org/"
    responce=requests.get(url)

    if responce.status_code==200:
        soup=BeautifulSoup(responce.text, "html.parser")
        letest_articles=[]

        for article in soup.select(".blog-widget li"):
            title=article.a.text.strip()
            letest_articles.append(title)
        return letest_articles
    else:
        print(f"failed to retrieve data.status code:{responce.status_code}") 
        return[]
