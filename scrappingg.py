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
    

if __name__=="__main__":
    python_articles = get_letest_python_articles()

    if python_articles:
        print("Latest article in the python selection:")
        for index, article in enumerate(python_articles,1):
            print(f"{index}.{article}")
    else:
        print("No articles found.")
