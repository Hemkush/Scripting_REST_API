from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = 'https://smith-maryland.12twenty.com/SalaryView/OutcomesIndex'
driver.maximize_window()
driver.get(url)

sleep(10)

directoryID = driver.find_element(By.XPATH, '//*[@id="username"]')
directoryID.send_keys('*********')

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('*********')

login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/form/div[4]/button')
login_button.click()

sleep(10)

device_button = driver.find_element(By.XPATH, '//*[@id="trust-browser-button"]')
device_button.click()



sleep(10)



