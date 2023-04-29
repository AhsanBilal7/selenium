import unittest
from selenium import webdriver
import page , locator
class pythonOrg(unittest.TestCase):
    def setUp(self):
        print("This is self")
        self.driver = webdriver.Chrome("D:\Graphic\SJCurve\selenium_python\chromedriver.exe")
        self.driver.get("http://orteil.dashnet.org/cookieclicker/")
    # def test_example(self):
    #     print("This is the test example")
    #     assert True
    # def test_example2(self):
    #     print("This is the F goto example")
    #     assert False
    # We have to keep in mind the naming convention name start with "test_"
    # Keep in mind with naming convention function name start with "test_"
    def test_title(self):        
        main = page.MainPage(self.driver)
        print("Statement before to check the page title")
        assert  main.is_page_match()
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()

