import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

service_obj = Service("C:\\Users\\Davoud\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)  #implicit wait

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
#//a[contains(@href,'shop')]

products = driver.find_elements(By.XPATH,"//app-card")

for product in products:
    productName = product.find_element(By.XPATH, "div/div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/div/button").click()

driver.find_element(By.XPATH, "//div/ul/li/a").click()
time.sleep(2)