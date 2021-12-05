import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager

#for using and introduce headless mode use options
options = webdriver.ChromeOptions()
options.headless = True
#same options is pass it over here
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(4)

"""half SS"""
#to capture half SS
driver.save_screenshot("halfImage.png")

"""Full SS"""
#make sure that you are running in headless mode
# take variable S, use JS(execute_script)

S = lambda X: driver.execute_script("return document.body.parentNode.scroll"+X)

#set the window size
driver.set_window_size(S("Width"), S("Height"))

#now use body.tagname because when u inspect the page, it starts from body tag.
driver.find_element(By.TAG_NAME, "body").screenshot("Full_Page_Screenshot.png")

driver.find_element(By.ID,"welcome").click()
driver.find_element(By.LINK_TEXT,"Logout").click()

time.sleep(4)
driver.quit()
print("Screenshot is added in the folder!!")