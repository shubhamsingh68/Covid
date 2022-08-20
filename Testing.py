import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.com")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("Cygnet Infotech")
driver.find_element(By.XPATH, "//input[@value='Google Search']").click()
driver.find_element(By.XPATH, "//h3[text()='Cygnet Infotech: Technology that moves business']").click()
expected_title = "Technology that moves business – Cygnet Infotech"
if driver.title == expected_title:
    print("Equal")
else:
    driver.quit()
