import time

import selenium as selenium
from selenium import webdriver

options = []

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
