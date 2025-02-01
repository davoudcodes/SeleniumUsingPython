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
time.sleep(2)