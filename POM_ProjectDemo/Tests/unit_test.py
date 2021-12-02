import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/santo/PycharmProjects/POM_Project/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        time.sleep(4)
        self.driver.find_element(By.ID, "welcome").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    @classmethod
    def tearDownClass(cls):
        # time.sleep(4)
        cls.driver.quit()
        print("Login Test successfully!")

if __name__ == '__main__':
    unittest.main()






