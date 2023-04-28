from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

#############


## GRABS THE BROWSER YOU WANT TO USE AND OPENS IT
thriveworks = webdriver.Edge()

##driver2 = webdriver.Edge()

def grab_sign_in_pages():
    
    thriveworks.get("https://accounts.google.com/v3/signin/identifier?dsh=S-15777518%3A1682441183857534&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AQMjQ7R3qty-9l3wsnRa1xK4eH861zs6F28P2usyq7AApuEoOvGWRH-wd4yjpTqnYVU6Bp4J8Wiwqg&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    # time.sleep(10)

    
    return thriveworks

def open_thriveworks():
    
    
    
    field_input = thriveworks.find_element(By.CLASS_NAME, 'whsOnd.zHQkBf')
    field_input.send_keys("shaun.tornilla@thriveworks.com")
    
    next_input = thriveworks.find_element(By.ID, 'identifierNext')
    next_input.click()
    
    time.sleep(5)

    field_input = thriveworks.find_element(By.CLASS_NAME, 'whsOnd.zHQkBf')
    field_input.send_keys("GuitarPlayer2022#")
    

    
    # next_input = thriveworks.find_element(By.ID, 'passwordNext')
    # next_input.click()
    
    ## HOW TO OPEN A TAB
    thriveworks.switch_to.new_window('tab')
    thriveworks.get("https://google.com")
    
    time.sleep(10)
    
    return 0




########## MAIN ##########

grab_sign_in_pages()

done = False

    
open_thriveworks()



time.sleep(10)