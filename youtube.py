from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
url = "https://www.youtube.com/"
driver.get(url)

searchbar = driver.find_element_by_id("search")
searchbar.send_keys("python beginners")

search = driver.find_element_by_id("search-icon-legacy")
search.submit()

video = driver.find_element_by_class_name("style-scope ytd-video-renderer")
video.click()