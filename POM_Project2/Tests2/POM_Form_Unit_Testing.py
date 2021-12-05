import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import HtmlTestRunner

class FormUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Chrome(executable_path="C:/Users/santo/PycharmProjects/POM_Project/drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_submit_form(self):
        driver = self.driver
        driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

        driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Hello")
        driver.find_element(By.ID, "RESULT_TextField-2").send_keys("World!!")
        driver.find_element(By.ID, "RESULT_TextField-3").send_keys("1234567890")
        driver.find_element(By.ID, "RESULT_TextField-4").send_keys("Sweden")
        driver.find_element(By.ID, "RESULT_TextField-5").send_keys("Malmö")
        driver.find_element(By.ID, "RESULT_TextField-6").send_keys("Sweden@gmail.com")
        # radio button
        driver.find_element(By.XPATH, "//label[contains(text(),'Female')]").click()
        # checkboxes
        driver.find_element(By.XPATH, "//label[contains(text(),'Monday')]").click()
        driver.find_element(By.XPATH, "//label[contains(text(),'Tuesday')]").click()
        driver.find_element(By.XPATH, "//label[contains(text(),'Wednesday')]").click()
        # driver.find_element(By.XPATH,"//label[contains(text(),'Monday')]").click()
        driver.find_element(By.XPATH, "//label[contains(text(),'Friday')]").click()
        # '//*[@id="q26"]/table/tbody/tr[1]/td/label'
        # driver.find_element(By.ID,"RESULT_RadioButton-9").click()

        # for select best time to call
        driver.find_element(By.XPATH, "//option[contains(text(),'Afternoon')]").click()
        # scroll down the page
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(6)
        driver.find_element(By.ID, "FSsubmit").click()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(4)
        cls.driver.quit()
        print("Test successfully!!")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/santo/PycharmProjects/POM_Project/POM_Project2/reportsOfProject2"))



