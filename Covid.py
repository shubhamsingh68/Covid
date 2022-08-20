from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.mygov.in/covid-19")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, "statewise-data").click()
cases = driver.find_elements(By.XPATH, "//table[contains(@class,'ind-mp_tbl')]/tbody/tr/td[4]/p/span")
state = driver.find_elements(By.XPATH, "//table[contains(@class,'ind-mp_tbl')]/tbody/tr/td[1]")
for i in range(0, len(cases)):
    txt = cases[i].text
    count = int(txt.replace(",", ""))
    if count >= 1000:
        ele = state[i].text
        print(ele + " " + txt)
