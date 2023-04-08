from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


## GRABS THE BROWSER YOU WANT TO USE AND OPENS IT
driver = webdriver.Edge()   

## PROVIDE URL FOR THE WINDOW TO OPEN INTO       
driver.get('file:///C:/Users/shaun/Desktop/CS/Personal%20Projects/Mechdyne/Projects/Files/ITW_Ticket_Layout.html#') 
## driver.get('https://google.com')       

time.sleep(10) 

def Subject_Section(input_dict):
    
    result_list = []
    
    print("\n\n\n==========\n\n\n")
    print(input_dict)
    print("\n\n\n==========\n\n\n")    
            
    ##user_input = input('\n\n\n==========\n\n\nUser Input: ')
    result_list.append(Subject_Row_Zero(input_dict["subject"]))
    ##user_input = input('\nPriority Level: ')
    result_list.append(Subject_Row_One(input_dict["priority"]))
    
    print("\n\n\n==========\n\n\n")
    print(result_list)
    print("\n\n\n==========\n\n\n")
    
    return result_list


def Subject_Row_Zero(user_input):
    
    print("\n\n\n==========\n\n\n")
    print(user_input)
    print("\n\n\n==========\n\n\n")
    
    ## Content Wrapper Main Box
    element = driver.find_element(By.ID, 'ContentWrapper')

    ## Grabs Form Structure
    sub_element_1 = element.find_element(By.ID, 'regform_id')

    ## Grabs top Section (Subject, Priority, Status, ABS Involved)
    sub_element_2 = sub_element_1.find_element(By.ID, 'StaticAreaDiv')

    ## Isolate the Variables to Manipulate
    sub_element_3 = sub_element_2.find_element(By.CLASS_NAME, 'dialog')

    ## Further Isolate Variables
    sub_element_4 = sub_element_3.find_element(By.CLASS_NAME, 'dialogMainContent')

    ## Grabs Table Variables Found In 
    sub_element_5 = sub_element_4.find_element(By.ID, 'table_992063')

    ## Isolate Row for Variable Manipulation
    sub_element_6 = sub_element_5.find_element(By.ID, 'row-0')

    ## USE TO INJECT SUBJECT NAME
    result = sub_element_6.find_element(By.CLASS_NAME, 'ticketTitleInput')
    
    result.send_keys(user_input)
    
    return result


def Subject_Row_One(user_input):
    
    print("\n\n\n==========\n\n\n")
    print(user_input)
    print("\n\n\n==========\n\n\n")
    
    ## Content Wrapper Main Box
    element = driver.find_element(By.ID, 'ContentWrapper')

    ## Grabs Form Structure
    sub_element_1 = element.find_element(By.ID, 'regform_id')

    ## Grabs top Section (Subject, Priority, Status, ABS Involved)
    sub_element_2 = sub_element_1.find_element(By.ID, 'StaticAreaDiv')

    ## Isolate the Variables to Manipulate
    sub_element_3 = sub_element_2.find_element(By.CLASS_NAME, 'dialog')

    ## Further Isolate Variables
    sub_element_4 = sub_element_3.find_element(By.CLASS_NAME, 'dialogMainContent')

    ## Grabs Table Variables Found In 
    sub_element_5 = sub_element_4.find_element(By.ID, 'table_992063')

    ## Isolate Row for Variable Manipulation
    sub_element_6 = sub_element_5.find_element(By.ID, 'row-1')
    
    select = Select(sub_element_6.find_element(By.CLASS_NAME, 'ticketField'))
    
    result = select.select_by_value(user_input)
    
    
    return result
    
#################### MAIN() ####################

input_dict = dict(
    subject = input("Subject: "),
    priority = input("Priority Value: ")
    ## status
    ## ABS Involved
)



submit_list = Subject_Section(input_dict)

print("\n\n\n==========\n\n\n")
print(submit_list)
print("\n\n\n==========\n\n\n")

## NOTE, for whatever reason there's an extra element in the array
## Removed with .pop() method for the following code to work.
## WILL LOOK INTO WHAT'S HAPPENING
submit_list.pop()

for element in submit_list:
        
    element.submit()
    
##submit_input.submit()



time.sleep(4)
driver.quit()

