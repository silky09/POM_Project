import time
from selenium import webdriver
#from selenium.webdriver.common.by import By
import unittest
from POM_ProjectDemo.Pages.loginPage import LoginPage
from POM_ProjectDemo.Pages.homePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/santo/PycharmProjects/POM_Project/drivers"
                                                      "/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_Login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(4)

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(4)
        cls.driver.quit()
        print("Login Test successfully!")

if __name__ == '__main__':
    unittest.main()






