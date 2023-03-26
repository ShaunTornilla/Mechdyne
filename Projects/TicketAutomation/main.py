from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
headlines = driver.find_elements_by
