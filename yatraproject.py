from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# opening chrome
driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
driver.get("https://www.yatra.com/")

# departure city

depart = driver.find_element_by_id("BE_flight_origin_city")
sleep(1)
depart.click()
sleep(1)
depart.send_keys("Chennai")
sleep(3)
depart.send_keys(Keys.ENTER)
sleep(2)

# arrival city

arrival = driver.find_element_by_id("BE_flight_arrival_city")
arrival.click()
sleep(1)
arrival.send_keys("Trivandrum")
sleep(2)
arrival.send_keys(Keys.ENTER)
sleep(2)

# clicking date

date = driver.find_element_by_id("BE_flight_origin_date")
date.click()
sleep(1)

# selecting date

selectdate = driver.find_element_by_id("10/06/2021")
selectdate.click()
sleep(1)

# clicking search btn

search = driver.find_element_by_id("BE_flight_flsearch_btn")
search.click()
sleep(1)

# using bs4 to fetch data

content = driver.page_source
yatra = BeautifulSoup(content, "html.parser")


# flight names

names_list = []
for flight_name in yatra.find_all('span', {'class': 'i-b text ellipsis'}):
    flight_names = flight_name.get_text()
    names_list.append(flight_names)
# print(names_list)

# arrival time
arrival_list = []
for arrival_time in yatra.find_all('p', {'class': 'bold fs-15 mb-2 pr time'}):
    arrtime = arrival_time.get_text()
    arrival_list.append(arrtime)
# print(arrival_list)

# price
price_list = []
for money in yatra.find_all('p', {'class': 'i-b tipsy fare-summary-tooltip fs-18'}):
    price = money.get_text()
    price_list.append(price)
# print(price_list)

# depart time
depart_list = []
for depart_time in yatra.find_all('div', {'class': 'i-b pr'}):
    dpttime = depart_time.get_text()
    depart_list.append(dpttime)


dp_list = []
for depart in range(len(depart_list)):
   dp_list.append(str(depart_list[depart])[0:5])

for i in range(len(names_list)):
    print("Flight Name = ", names_list[i], "Departure Time = ", dp_list[i], "Arrival Time = ", arrival_list[i], "Price = ", price_list[i])