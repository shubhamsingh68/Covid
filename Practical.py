from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://datatables.net/")
driver.implicitly_wait(10)
drop = Select(driver.find_element(By.NAME, "example_length"))
drop.select_by_visible_text("100")
rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
for i in rows:
    td = i.find_elements(By.TAG_NAME, "td")
    txt = ""
    for j in td:
        txt = txt + str(j.text) + " "
    print(txt)
driver.quit()
