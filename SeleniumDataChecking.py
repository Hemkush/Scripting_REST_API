from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.phptravels.net')

# b_tags = driver.find_elements_by_tag_name('b')
b_tags = driver.find_elements("tag name", "small")

sleep(3)
price_list = []
for b in b_tags:
    price_list.append(b.text)
print("Prices: ",price_list)

clean_price_list =[]
for price in price_list:
    if price.startswith('From USD'):
        price_number = price
        integer_price = price_number.replace('From ', '')
        clean_price_list.append(integer_price)

print (sorted(clean_price_list))