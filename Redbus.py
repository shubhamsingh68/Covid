from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import datetime

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://redbus.in/")
driver.implicitly_wait(30)
driver.find_element(By.ID, "src").send_keys("Mumbai")
# driver.find_element(By.XPATH, "//i[text()='Mumbai']").click()
driver.find_element(By.ID, "dest").send_keys("Pune")
# driver.find_element(By.XPATH, "//i[text()='Pune']").click()
driver.find_element(By.ID, "onward_cal").click()
current_time = datetime.datetime.now()
current_date = current_time.day
driver.find_element(By.XPATH, "//td[@class='current day']").click()
driver.find_element(By.ID, "search_btn").click()

driver.find_element(By.XPATH, "//div[@class='close-primo']").click()
ratings = driver.find_elements(By.XPATH, "//div[contains(@class,'rating-sec')]//div//i")
for i in ratings:
    print(i.text)