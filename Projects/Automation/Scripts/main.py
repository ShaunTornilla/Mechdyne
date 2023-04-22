from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


## GRABS THE BROWSER YOU WANT TO USE AND OPENS IT
driver = webdriver.Edge()   

## PROVIDE URL FOR THE WINDOW TO OPEN INTO       
driver.get('file:///C:/Users/shaun/Desktop/CS/Personal%20Projects/Mechdyne/Projects/Files/ITW_Ticket_Layout.html#') 
## driver.get('https://google.com')       

## Uncomment in case you need the terminal to output clean
time.sleep(10) 

## To see the before and after of the ticket template
## time.sleep(2)

## Content Wrapper Main Box and form structure as "global variable" for following functions
search_variable = driver.find_element(By.ID, 'ContentWrapper').find_element(By.ID, 'regform_id')


def Form_Input(input_dict):
    
    result_list = []

    ## Subject Section
    result_list.append(Subject_Row_Zero(input_dict["subject"]))
    result_list.append(Subject_Row_One(input_dict["priority"], input_dict["status"], input_dict["abs_involved"]))
    
    ## Ticket Information
    result_list.append(Ticket_Information(input_dict["service_type"], input_dict["issue_type"]))
    
    
    
    return result_list


def Subject_Row_Zero(subject):
    
    # print("\n\n\n==========\n\n\n")
    # print(user_input)
    # print("\n\n\n==========\n\n\n")
    
    ## Grabs top Section (Subject, Priority, Status, ABS Involved)
    search_element = search_variable.find_element(By.ID, 'StaticAreaDiv')

    ## Isolate the Variables to Manipulate
    search_sub_element = search_element.find_element(By.CLASS_NAME, 'dialog')

    ## Further Isolate Variables
    search_sub_element_2 = search_sub_element.find_element(By.CLASS_NAME, 'dialogMainContent')

    ## Grabs Table Variables Found In 
    search_sub_element_3 = search_sub_element_2.find_element(By.ID, 'table_992063')

    ## Isolate Row for Variable Manipulation
    search_sub_element_4 = search_sub_element_3.find_element(By.ID, 'row-0')

    ## USE TO INJECT SUBJECT NAME
    result = search_sub_element_4.find_element(By.CLASS_NAME, 'ticketTitleInput')
    
    result.send_keys(subject)
    
    return result


def Subject_Row_One(priority, status, abs_involved):
    
    # print("\n\n\n==========\n\n\n")
    # print(user_input)
    # print("\n\n\n==========\n\n\n")

    ## Grabs top Section (Subject, Priority, Status, ABS Involved)
    search_element = search_variable.find_element(By.ID, 'StaticAreaDiv')

    ## Isolate the Variables to Manipulate
    search_sub_element = search_element.find_element(By.CLASS_NAME, 'dialog')

    ## Further Isolate Variables
    search_sub_element_2 = search_sub_element.find_element(By.CLASS_NAME, 'dialogMainContent')

    ## Grabs Table Variables Found In 
    search_sub_element_3 = search_sub_element_2.find_element(By.ID, 'table_992063')

    ## Isolate Row for Variable Manipulation
    row_layout = search_sub_element_3.find_element(By.ID, 'row-1')
    
    ## To Update Priority ##
    row_layout_element = row_layout.find_element(By.ID, 'priCell')
    select = Select(row_layout_element.find_element(By.ID, 'pri'))
    return_priority = select.select_by_value(priority)
    
    ## To Update Status ##
    row_layout_element = row_layout.find_element(By.ID, 'statCell')
    select = Select(row_layout_element.find_element(By.ID, 'status'))
    return_status = select.select_by_value(status)
    
    ## To Update ABS_Involved ##
    row_layout_element = row_layout.find_element(By.ID, 'yui_3_18_1_2_1680139374228_184')
    select = Select(row_layout_element.find_element(By.ID, 'ABS__bInvolved'))
    return_abs_involved = select.select_by_value(abs_involved)
    

    return return_priority, return_status, return_abs_involved


def Ticket_Information(service_request, issue_type):
    
    ## TO DO
    search_element = search_variable.find_element(By.ID, 'VerticalTabsAndMenuHolder')
    
    search_sub_element_2 = search_element.find_element(By.ID, 'FIELD_DIALOG_0')
    
    ## FOUND IN "TicketInformation_ecTable" table type
    search_sub_element_3 = search_sub_element_2.find_element(By.CLASS_NAME, 'dialogMainContent')
    
    search_sub_element_4 = search_sub_element_3.find_element(By.ID, 'table_555737')
    
    row_count = search_sub_element_4.find_elements(By.TAG_NAME, "fieldset")
    
    print("\n=========\n\n")
    count = 0
    for element in row_count:
        count+=1
        
    print("Row Count: ", count)
    
    
    
    ## Service Type (Make a Selection)
    # row = search_sub_element_4.find_element(By.ID, 'row-1')
    # row_one_element = row.find_element(By.CLASS_NAME, 'fieldInput')
    # select = Select(row_one_element.find_element(By.ID, 'Service__bType'))
    # return_row_one = select.select_by_value(service_request)
    
    # ## Type
    # row = search_sub_element_4.find_element(By.ID, 'row-2')
    # row_two_element =  row.find_element(By.CLASS_NAME, 'fieldInput')
    # select = Select(row_two_element.find_element(By.ID, 'Type'))
    # return_row_two = select.select_by_value(issue_type)
    
    # print("\n\n\n==========\n\n\n")
    # print(row_two_element)
    # print("\n\n\n==========\n\n\n")
    
    return 0#return_row_one##, return_row_two

#################### MAIN() ####################

# input_dict = dict(
#     subject = input("Subject: "),
#     priority = input("Priority Value: "),
#     status = input("Status: ")
#     ## ABS Involved
# )

input_dict = dict(
    
    ## Subject Section
    subject = "Dickslap",
    priority = "3",
    status = "In__bProcess",
    abs_involved = "Yes",
    service_type = "Service__bRequest",
    issue_type = "Password__bResets"
)

##submit_list = []

submit_list = Form_Input(input_dict)

print("\n\n\n==========\n\n\n")
print(submit_list)
print("\n\n\n==========\n\n\n")

## NOTE, for whatever reason there's an extra element in the array
## Removed with .pop() method for the following code to work.
## WILL LOOK INTO WHAT'S HAPPENING... eventually maybe not, whatever
submit_list.pop()
submit_list.pop()

for element in submit_list:
        
    element.submit()
    
##submit_input.submit()



time.sleep(5)
driver.quit()

