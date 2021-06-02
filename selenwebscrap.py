from selenium import webdriver
from bs4 import BeautifulSoup

# USING SELENIUM AND BS4
driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
url = 'https://www.myntra.com/bags'
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")

# TO FETCH DATA
for text in soup.find_all('div',{'class':'product-price'}):
    print(text.span.text)
