from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.google.com/")
headlines = driver.find_elements
