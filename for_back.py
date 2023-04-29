from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

Path = "D:\Graphic\SJCurve\selenium_python\chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.get("https://www.techwithtim.net/")
wait = WebDriverWait(driver,10)
link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Python Programming")))
# Keep in mind that By Method after the EC.element find has 2 brackets
link.click()
try:
    element = wait.until(EC.element_to_be_clickable( (By.LINK_TEXT,"Beginner Python Tutorials")))
    print("It is located")
    element.click()
    time.sleep(5)
    driver.back()
except:
    print("It is not located")
    driver.quit()
