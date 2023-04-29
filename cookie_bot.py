from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC

Path = "D:\Graphic\SJCurve\selenium_python\chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.get("http://orteil.dashnet.org/cookieclicker/")
# wait = WebDriverWait(driver,10)
time.sleep(5)
wait = WebDriverWait(driver , 10)
english = wait.until(EC.presence_of_element_located((By.ID, "langSelect-EN")))

english.click()
# driver.implicitly_wait(5)
cookie = wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))
cookie_count = wait.until(EC.presence_of_element_located((By.ID, "cookies")))

items = []
# for i in range(1, -1, -1):
#     item = driver.find_element(By.ID, f"productPrice{i}")
#     items.append(item)
items = [driver.find_element(By.ID, "productPrice1") , driver.find_element(By.ID, "productPrice0")]

print(items)
action = ActionChains(driver)
for i in range (5000):
    action.click(cookie)
    action.perform()
    count = int (cookie_count.text.split(" ")[0]) 
    for item in items:
        value = int(item.text)
        if value <= count:
            update_action = ActionChains(driver)
            update_action.move_to_element(item)
            update_action.click(item)
            update_action.perform()
            
            

    