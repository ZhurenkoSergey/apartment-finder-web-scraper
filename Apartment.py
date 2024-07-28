import requests
from bs4 import BeautifulSoup

url = 'https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
link = 'https://www.olx.ua'+soup.find('div', class_='css-1sw7q4x').find('a', class_='css-z3gu2d').get('href')
print(link)