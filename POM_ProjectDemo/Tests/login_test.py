import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/santo/PycharmProjects/POM_Project/drivers/chromedriver.exe")

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(4)
driver.find_element(By.ID,"welcome").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
#time.sleep(4)
driver.quit()
print("Login Test successfully!")



