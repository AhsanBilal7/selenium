from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
PATH = "D:\Graphic\SJCurve\selenium_python\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.w3schools.com/")
print(driver.title)
search = driver.find_elements(By.ID, "search2")[0]
search.send_keys("test")
search.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()