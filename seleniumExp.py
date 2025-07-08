from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://google.com")

# Find the search box using its name attribute value
search_box = driver.find_element("name", "q")
search_box.send_keys("test")

search_box.send_keys(Keys.RETURN)

sleep(5)

driver.quit()