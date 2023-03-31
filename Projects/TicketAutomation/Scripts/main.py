from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


## GRABS THE BROWSER YOU WANT TO USE AND OPENS IT
driver = webdriver.Edge()   

## PROVIDE URL FOR THE WINDOW TO OPEN INTO       
driver.get('https://google.com')    


## SEARCH FOR ELEMENT IN HTML FILE BY ITS NAME
element = driver.find_element(By.NAME, 'q')

## EDIT THE VALUE
element.send_keys('youtube')

element.submit()

## EXTRACT THE FUCK OUT OF WHAT YOU NEED TO CLICK
element = driver.find_element(By.CLASS_NAME, 'MjjYud').find_element(By.CLASS_NAME, 'yuRUbf').find_element(By.TAG_NAME, 'h3')



print("\n\n\nDICKSLAP\n\n\n")
print(element)
print("\n\n\nDICKSLAP\n\n\n")

element.click()

time.sleep(6)
driver.quit()

