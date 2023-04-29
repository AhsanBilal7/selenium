from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Path = "D:\Graphic\SJCurve\selenium_python\chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.get("https://www.techwithtim.net/")
# search = driver.find_elements(By.ID, "s")[0]
# search.send_keys("test")
# search.send_keys(Keys.RETURN)
# time.sleep(5)
# try:
#     main = WebDriverWait(driver,10).until(
#         # EC.visibility_of_element_located((By.NAME ,'s'))
#         driver.find_elements(By.ID, "s")[0]
#         )
#     main = main[0]
#     main.send_keys("Test Time")
#     main.send_keys(Keys.RETURN)
#     time.sleep(5) 
#     print(main.text)
# except ValueError:
#     print("Value has the error")
# finally:
#     driver.quit()


try:
    # navigate to the website
    # driver.get("https://www.example.com")

    # find the search box element by ID
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "s")))
    search_box.clear()
    # enter the search text and submit
    search_box.send_keys("test")
    search_box.send_keys(Keys.RETURN)

    # wait for the search results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main")))

    # get the search result element and print its text
    search_result = driver.find_element(By.ID, "main")
except Exception as e:
    print("Error occurred:", e)

finally:
    # close the driver instance
    driver.quit()
    print("Yes the main is present")