from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time, re


class Test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/drivers/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_2(self):
        driver = self.driver
        driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        driver.find_element(By.ID, "RESULT_TextField-1").click()
        driver.find_element(By.ID, "RESULT_TextField-1").clear()
        driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Silky")
        driver.find_element(By.ID, "RESULT_TextField-2").click()
        driver.find_element(By.ID, "RESULT_TextField-2").clear()
        driver.find_element(By.ID, "RESULT_TextField-2").send_keys("s")
        driver.find_element(By.ID, "RESULT_TextField-3").click()
        driver.find_element(By.ID, "RESULT_TextField-3").clear()
        driver.find_element(By.ID, "RESULT_TextField-3").send_keys("0987654321")
        driver.find_element(By.ID, "RESULT_TextField-4").clear()
        driver.find_element(By.ID, "RESULT_TextField-4").send_keys("sweden")
        driver.find_element(By.ID, "RESULT_TextField-5").clear()
        driver.find_element(By.ID, "RESULT_TextField-5").send_keys("staffanstorp")
        driver.find_element(By.ID, "RESULT_TextField-6").clear()
        driver.find_element(By.ID, "RESULT_TextField-6").send_keys("s@gmail.com")
        driver.find_element(By.XPATH, "//div[@id='q26']/table/tbody/tr[2]/td/label").click()
        driver.find_element(By.XPATH, "//div[@id='q15']/table/tbody/tr[2]/td/label").click()
        driver.find_element(By.XPATH, "//div[@id='q15']/table/tbody/tr[3]/td/label").click()
        driver.find_element(By.XPATH, "//div[@id='q15']/table/tbody/tr[4]/td/label").click()
        driver.find_element(By.XPATH, "//div[@id='q15']/table/tbody/tr[5]/td/label").click()
        driver.find_element(By.XPATH, "//div[@id='q15']/table/tbody/tr[6]/td/label").click()
        driver.find_element(By.XPATH, "//div[@id='q15']/table/tbody/tr[7]/td/label").click()
        driver.find_element(By.ID, "RESULT_RadioButton-9").click()
        Select(driver.find_element(By.ID, "RESULT_RadioButton-9")).select_by_visible_text("Morning")
        time.sleep(5)
        driver.find_element(By.ID, "FSsubmit").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
