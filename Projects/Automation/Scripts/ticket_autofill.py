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
##time.sleep(10) 

## To see the before and after of the ticket template
## time.sleep(2)

# ## Content Wrapper Main Box and form structure as "global variable" for following functions
# search_variable = driver.find_element(By.ID, 'ContentWrapper').find_element(By.ID, 'regform_id')

search_variable = driver.find_element(By.ID, 'regform_id')


def Form_Input(input_dict):
    
    result_list = []

    ## Subject Section
    result_list.append(Subject_Section(input_dict["subject"], input_dict["priority"], input_dict["status"], input_dict["abs_involved"]))
        
    ## Ticket Information,
    result_list.append(Ticket_Information(input_dict["service_type"], input_dict["issue_type"]))
    
    ## Description
    result_list.append(Description(input_dict["security_incident"],input_dict["ticket_description"], input_dict["internal_notes"]))
    
    
    ##input_dict["service_type"]
    
    return result_list


def Subject_Section(subject, priority, status, abs_involved):

    result = search_variable.find_element(By.CLASS_NAME, 'ticketTitleInput')
    result.send_keys(subject)
    
    ## To Update Priority ##
    select = Select(search_variable.find_element(By.ID, 'pri'))
    return_priority = select.select_by_value(priority)
    
    ## To Update Status ##
    select = Select(search_variable.find_element(By.ID, 'status'))
    return_status = select.select_by_value(status)
    
    # ## To Update ABS_Involved ##
    select = Select(search_variable.find_element(By.ID, 'ABS__bInvolved'))
    return_abs_involved = select.select_by_value(abs_involved)

    return 0    
    # return result
    
def Ticket_Information(service_type, issue_type):
    
    ## To Update Service Type ##
    service_type_field = search_variable.find_element(By.ID, 'Service__bType')
    service_type_field.send_keys(service_type)
    
    ## To Update Issue Type ##
    issue_type_field = search_variable.find_element(By.ID, 'Type')
    issue_type_field.send_keys(issue_type)
    
    # print("\n\n\n")
    # print(issue_type_field)
    # print("\n\n\n")
    
    return 0

def Description(security_incident, ticket_description, internal_notes):
    
    ## To Update Security Incident ##
    service_incident_field = search_variable.find_element(By.ID, "Is__bthis__ba__bSecurity__bIncident__Q")
    service_incident_field.send_keys(security_incident)

    ## To Input Description of Problem ##
    # ticket_description_field = search_variable.find_element(By.TAG_NAME, "document")
    # ticket_description_field.send_keys("SHAUN IS A SCRUBLORD AND A DICKSLAP")
    
    
    ## To Input Internal Notes ##
    # internal_notes_field = search_variable.find_element(By.ID, "table_339773").find_element(By.ID, "row-1")
    internal_notes_field = search_variable.find_element(By.ID, "Internal__bNotes")
    internal_notes_field.send_keys(internal_notes)


    print("\n\n\n")
    print(internal_notes_field)
    print("\n\n\n")         
    
    return 0
    
def Contact_Information():
    
    ## To Input Employee ID and use the Built-In Search ##
    
    
    
    
    return 0

def Technician_Notifications():
    
    ## Update Technicians ##

    
    
    
    return 0

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
    issue_type = "Password__bResets",
    security_incident = "Yes",
    ticket_description = "",
    internal_notes = "SHAUN IS A SCRUBLORD AND A DICKSLAP"
)

##submit_list = []

submit_list = Form_Input(input_dict)

## NOTE, for whatever reason there's an extra element in the array
## Removed with .pop() method for the following code to work.
## WILL LOOK INTO WHAT'S HAPPENING... eventually maybe not, whatever
submit_list.pop()
submit_list.pop()

# for element in submit_list:
        
#     element.submit()
    
# ##submit_input.submit()



time.sleep(5)
driver.quit()

