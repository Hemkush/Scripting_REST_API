from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
driver.get('https://www.seleniumhq.org')

element = driver.find_element(By.XPATH, '/html/body/div/main/section[2]/div/div/div[1]/div/div[2]/div/a')

element.click()
sleep(2)

# search_element = driver.find_element_by_id('q')

# search_element.send_keys('webdriver')

# go_button = driver.find_element_by_id('submit')

# go_button.click()



# sleep(1)
# driver.switch_to.frame('master-1')

# link_elements = driver.find_elements_by_tag_name('a')

# print(link_elements[0].get_attribute('href'))