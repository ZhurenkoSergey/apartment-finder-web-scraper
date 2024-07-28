import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

data = []

for i in range(1,26):
    print(i)
    url = 'https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev/'
    response = requests.get(url)
    sleep(3)
    soup = BeautifulSoup(response.text,'lxml')
    Apartments = soup.findAll('div', class_='css-1sw7q4x')

for Apartment in Apartments:

    try:
        name = Apartment.find('h6', class_='css-1wxaaza').text
        price = Apartment.find('p', class_='css-13afqrm').text
        link = 'https://www.olx.ua' + Apartment.find('a', class_='css-z3gu2d').get('href')
    except:
        name = '--'
        price = '--'
        link = '--'
    data.append([name, price, link])


print(data)
header = [['Адреса', 'Ціна', 'Посилання']]
df = pd.DataFrame(data, columns=header)
df.to_csv('/Users/Gyrocopter_UA/Desktop/Apartment.csv', sep =';', encoding ='ansi')