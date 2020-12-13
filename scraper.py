import requests
from bs4 import BeautifulSoup

URL = 'http://www.cukashmir.ac.in/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# Finding result
results = soup.find(id='whats')

news = results.find_all('div', class_='labeltext')

# creating response array
data_list = []
# print(news)
for item in news:
    # making it neet
    item_link = item.find('a', class_='labellink')
    data_list.append([item.text[:-10], item_link.get('href')])

# converting data-list to json
# json = json.dumps(data_list)

# print(json)
