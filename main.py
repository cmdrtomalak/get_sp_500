import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable sortable'})

for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    if len(cells) > 0:
        ticker_symbol = cells[0].text.strip()
        print(ticker_symbol)
