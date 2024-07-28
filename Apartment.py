import requests
from bs4 import BeautifulSoup

url = 'https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
name = soup.find('div',class_='css-1sw7q4x').find('h6',class_='css-1wxaaza').text
price = soup.find('div', class_='css-1sw7q4x').find('p', class_='css-13afqrm').text
link = 'https://www.olx.ua'+soup.find('div', class_='css-1sw7q4x').find('a', class_='css-z3gu2d').get('href')
print(name)
print(price)
print(link)
