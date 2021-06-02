from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=table&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
lines = requests.get(url)
code = lines.text
flipkart = BeautifulSoup(code, "html.parser")

# TO FETCH DATA
for text in flipkart.find_all('a', {'class': 's1Q9rs'}):
    table = text.string
    print(table)
for price in flipkart.find_all('div', {'class': '_30jeq3'}):
    cost = price.string
    print(cost)
