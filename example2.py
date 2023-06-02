# python -m pip install selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/search?sxsrf=APwXEddksiFahDAPaWjeoeh1IyxKI7XJWg:1685686857890&q=%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C+%D0%BC%D0%BE%D1%80%D1%81%D0%BA%D0%B8%D0%B5+%D0%BF%D0%B5%D0%B9%D0%B7%D0%B0%D0%B6%D0%B8+%D0%BC%D0%B0%D1%81%D0%BB%D0%BE%D0%BC&tbm=isch&chips=q:%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C+%D0%BC%D0%BE%D1%80%D1%81%D0%BA%D0%B8%D0%B5+%D0%BF%D0%B5%D0%B9%D0%B7%D0%B0%D0%B6%D0%B8+%D0%BC%D0%B0%D1%81%D0%BB%D0%BE%D0%BC,online_chips:%D1%81%D0%BE%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D1%85+%D1%85%D1%83%D0%B4%D0%BE%D0%B6%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2:6ztMT_LccK4%3D&usg=AI4_-kSj47vIITs08Dx2vk-K7f_d-LyEwQ&sa=X&ved=2ahUKEwiGuvfy-KP_AhVlx4sKHQ0fD7QQgIoDKAB6BAgcEBI&biw=1280&bih=577&dpr=1.5")



time.sleep(2)

# 👇️ using find_element method 👇️
search_field = driver.find_elements(By.XPATH, "//*[@class=\"rg_i Q4LuWd\"]")


driver.save_screenshot('sea.png')

time.sleep(2)

driver.close()