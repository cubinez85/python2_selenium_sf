# python -m pip install selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

time.sleep(2)

# 👇️ using find_element method 👇️
search_field = driver.find_element(By.NAME, 'q')

search_field.send_keys('Skillfactory')

driver.save_screenshot('sf.png')

search_field.submit()

time.sleep(2)

driver.close()