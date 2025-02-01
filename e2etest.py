import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "input[id='country']").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in successText

time.sleep(2)