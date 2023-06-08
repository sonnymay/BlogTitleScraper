import requests
from bs4 import BeautifulSoup

# URL to be scraped
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# Send a HTTP request to the URL
response = requests.get(url)

# If request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    for article_title in soup.find_all('h2'):
        print(article_title.get_text())
else:
    print(f'Failed to retrieve the webpage: {response.status_code}')