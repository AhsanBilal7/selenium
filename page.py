class BasePage():
    def __init__(self , driver):
        self.driver = driver
        
class MainPage(BasePage):
    def is_page_match(self):
        return "Cookie" in self.driver.title
    def click_go_element(self):
        element = self.driver.find_element()
        element.click()