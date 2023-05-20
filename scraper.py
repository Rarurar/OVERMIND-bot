import requests
from bs4 import BeautifulSoup


valutes = {"UAH": 0,   # Кількість гривень в доларі
           "PLN": 0,    # Кількість злотих в доларі
           "CHF": 0,    # Кількість франків в доларі     # Словник, що буде використовуватись основною частиною програми
           "RUB": 0,   # Кількість рублів в доларі
           "EUR": 0,    # Кількість євро в доларі
           "USD": 1}   # Значення долара


URL = "https://www.theglobaleconomy.com/rankings/Dollar_exchange_rate/"    # Посилання на сайт з курсом валют
'''
Залишок програми оброблює дані з сайту і змінює значення в словнику valutes згідно з актуальним курсом валют
'''
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
currencies = (soup.find_all(id='benchmarkTable', class_="sortable"))
crs = currencies[0]
crs = crs.find_all('td', string=True)
a = []
for i in crs:
    a.append(i.string)
cj = 0
for j in a:
    if j == 'Ukraine':
        valutes['UAH'] = a[cj+1]
    if j == 'Poland':
        valutes['PLN'] = a[cj+1]
    if j == 'France':
        valutes['CHF'] = a[cj+1]
    if j == 'Russia':
        valutes['RUB'] = a[cj+1]
    if j == 'Euro area':
        valutes['EUR'] = a[cj+1]
    cj += 1
