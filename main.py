import time
from select import select

import selenium as selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

options = []

#driver options
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
driver.implicitly_wait(5)
action = ActionChains(driver)

#window details
window_before = driver.window_handles[0]  # to get handle of parent window
window_before_title = driver.title
print(window_before_title)
print(driver.current_url)


#mouse hover
action.move_to_element(driver.find_element_by_xpath("//a[@class='dropdown-toggle meganav-shop']")).perform()
action.move_to_element(driver.find_element_by_link_text("Foodgrains, Oil & Masala")).perform()
driver.find_element_by_link_text("Dry Fruits").click()


#static dropdown
dropdown = Select(driver.find_element_by_xpath("//select[@ng-model='vm.sortOrder']"))
dropdown.select_by_index(2)


#clicking checkboxes
#driver.find_element_by_xpath("//i[@class='cr-icon fa fa-check']").click()


#length of checkboxes
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))


#dynamic dropdown
driver.find_element_by_xpath("//input[@value='Search by Brand']").send_keys("delishh")
time.sleep(4)
driver.find_element_by_xpath("//span[@ng-bind='brand.display_name']").click()
time.sleep(3)
driver.find_element_by_xpath("//a[@uib-tooltip='Frozen Blackberries']").click()
driver.find_element_by_xpath("//div[@data-qa='addToBasket']").click()
time.sleep(3)


#adding item to cart
driver.find_element_by_xpath("//input[@id='productSearch']").send_keys("Fruit Juice - Delight, Litchi")
driver.find_element_by_xpath("//button[@type='submit']").click()

driver.find_element_by_xpath("//i[@class='fa fa-caret-down']/parent::button").click()
driver.find_element_by_partial_link_text("2x1 L").click()
driver.find_element_by_xpath("//button[@type='button']/parent::div[@class='col-sm-5 col-xs-5 pad-0']").click()

driver.find_element_by_xpath("//a[@href='/?nc=logo']").click()
driver.find_element_by_xpath("//span[@class='basket-content']").click()
driver.find_element_by_xpath("//button[@qa='viewBasketMB']").click()










