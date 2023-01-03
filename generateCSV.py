import random
import csv


# number of rows in each entity
numOfDeptartments = 10000
numOfEmployees = 100000
numOfBranchs = 10000
numOfCustomers = 200000
numberOfPlans = 10000
numOfCards = 100000
numOfServices = 100000
numOfComplaints = 100000
numOfFaqs = 100000
numOfOffers = 10000


# number of rows in each relation
numOfCustomerOffer = 1000000
numOfCustomerService = 1000000

# customer
max_mins_used = 1000000
max_megas_used = 100000000
max_balance = 10000

# card
max_card_value = 10000
min_card_value = 10
recharged_cards_ids = []

# service
max_service_cost = 400
min_service_cost = 10

# offers
max_offer_price = 10000
min_offer_price = 10
min_offer_minutes = 10
max_offer_minutes = 1000
min_offer_megas = 10
max_offer_megas = 10000


# department
managers_ssn_list = [0] * numOfDeptartments


# plan
min_plan_cost = 10
max_plan_cost = 1000
min_plan_minutes = 10
max_plan_minutes = 1000
min_plan_megas = 10
max_plan_megas = 10000


##############################################################################
currPhoneNumber = 1000000000
def generatePhoneNumber():
    global currPhoneNumber
    currPhoneNumber += 1
    return '0' + str(currPhoneNumber)


def generateRandomDate():
    year = random.randint(2015, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return str(year) + '-' + str(month) + '-' + str(day)
##############################################################################


def generateEmployeeData():
    employeeData = []
    for i in range(1,numOfEmployees +1):
        # SSN, FIRST_NAME, LAST_NAME, DEPT_NUM, SALARY, GENDER, PHONE_NUM, BRANCH, MGR_SSN
        department = random.randint(1, numOfDeptartments+1)
        if i == 1:
            employeeData.append(['SSN', 'FIRST_NAME', 'LAST_NAME', 'DEPT_NUM', 'SALARY', 'GENDER', 'PHONE_NUM', 'BRANCH','MGR_SSN'])
        employeeData.append([i, "FIRST_NAME" + str(i), "LAST_NAME" + str(i), department, random.randint(5000 , 50001) ,random.choice(['M','F']), generatePhoneNumber(), random.randint(1, numOfBranchs+1), managers_ssn_list[department-1]])
    return employeeData


def generateCustomerData():
    customerData = []
    for i in range(1, numOfCustomers + 1):
        # ID, FIRST_NAME, LAST_NAME, GENDER, PHONE_NUMBER, USED_MINS, USED_MEGAS, BALANCE, PLAN_ID
        if i == 1:
            customerData.append(['ID', 'FIRST_NAME', 'LAST_NAME', 'GENDER', 'PHONE_NUMBER', 'USED_MINS', 'USED_MEGAS', 'BALANCE', 'PLAN_ID'])
        customerData.append([i, "FIRST_NAME" + str(i), "LAST_NAME" + str(i), random.choice(['M','F']), generatePhoneNumber(), random.randint(0,max_mins_used),random.randint(0,max_mins_used),random.randint(0,max_balance),random.randint(1,numberOfPlans)])
    return customerData



def generateDepartmentData():
    departmentData = []
    for i in range(1, numOfDeptartments + 1):
        # DNUM, DNAME, MGR_SSN
        if i == 1:
            departmentData.append(['DNUM', 'DNAME', 'MGR_SSN'])
        mng_ssn = random.randint(1, numOfEmployees+1)
        managers_ssn_list.append(mng_ssn)
        departmentData.append([i, "DEPT" + str(i), mng_ssn])
    return departmentData


def generateCardData():
    cardData = []
    for i in range(1, numOfCards + 1):
        # SERIAL_NUM, VALUE, IS_RECHARGED, CUSTOMER_ID
        if i == 1:
            cardData.append(['SERIAL_NUM', 'VALUE', 'IS_RECHARGED', 'CUSTOMER_ID'])
        is_recharged = random.choice([0, 1])
        if is_recharged == 1:
            recharged_cards_ids.append(i)
        cardData.append([i, random.randint(min_card_value, max_card_value), is_recharged, random.randint(1, numOfCustomers+1) if is_recharged == 1 else None])
    return cardData


def generateServiceData():
    serviceData = []
    for i in range(1, numOfServices + 1):
        # SERVICE_ID, COST_ID, DESCRIPTION_ID
        if i == 1:
            serviceData.append(['SERVICE_ID', 'COST', 'DESCRIPTION_ID'])
        serviceData.append([i, random.randint(min_service_cost, max_service_cost), 'DESCRIPTION' + str(i)])
    return serviceData

def generateCompliantsData():
    complaintsData = []
    for i in range(1, numOfComplaints + 1):
        # CODE, STATUS, DESCRIPTION, DATE, CUSTOMER_ID, EMPLOYEE_ID, EMPLOYEE_FIRST_NAME, EMPLOYEE_LAST_NAME
        employeeId = random.randint(1, numOfEmployees+1)
        if i == 1:
            complaintsData.append(['CODE', 'STATUS', 'DESCRIPTION', 'DATE', 'CUSTOMER_ID', 'EMPLOYEE_ID', 'EMPLOYEE_FIRST_NAME', 'EMPLOYEE_LAST_NAME'])
        complaintsData.append([i,random.choice([0,1]), 'COMPLAINT' + str(i), generateRandomDate(), random.randint(1, numOfCustomers+1), employeeId,"FIRST_NAME" + str(employeeId), "LAST_NAME" + str(employeeId)])
    return complaintsData

def generateBranchData():
    branchData = []
    for i in range(1, numOfBranchs + 1):
        # BNUM, DNUM, PHONE_NUM, LOCATION
        if i == 1:
            branchData.append(['BNUM', 'PHONE_NUM', 'LOCATION'])
        branchData.append([i, generatePhoneNumber(), 'LOCATION' + str(i)])
    return branchData

def generateOfferData():
    offerData = []
    for i in range(1, numOfOffers + 1):
        # ID, PRICE, MINUTES, MEGAS, EXPIRE_DATE
        if i == 1:
            offerData.append(['ID', 'PRICE', 'MINUTES', 'MEGAS', 'EXPIRE_DATE'])
        offerData.append([i, random.randint(min_offer_price, max_offer_price+1), random.randint(min_offer_minutes, max_offer_minutes+1), random.randint(min_offer_megas, max_offer_megas+1), generateRandomDate()])
    return offerData

def generateFAQData():
    faqData = []
    for i in range(1, numOfFaqs + 1):
        # ID, QUESTION, ANSWER, IS_ANSWERED, SSN, DATE
        if i == 1:
            faqData.append(['ID', 'QUESTION', 'ANSWER', 'IS_ANSWERED', 'SSN', 'DATE'])
        is_answered = random.choice([0, 1])
        faqData.append([i, 'QUESTION' + str(i), 'ANSWER' + str(i), is_answered, random.randint(1, numOfEmployees+1) if is_answered == 1 else None, generateRandomDate()])
    return faqData

def generatePlanData():
    planData = []
    for i in range(1, numberOfPlans + 1):
        # ID, COST, MINUTES, MEGAS
        if i == 1:
            planData.append(['ID', 'COST', 'MINUTES', 'MEGAS'])
        planData.append([i, random.randint(min_plan_cost, max_plan_cost), random.randint(min_plan_minutes, max_plan_minutes), random.randint(min_plan_megas, max_plan_megas)])
    return planData


def generateCustomer_OfferData():
    customer_offerData = []
    for i in range(1, numOfCustomerOffer + 1):
        # ID, CUSTOMER_ID, OFFER_ID
        if i == 1:
            customer_offerData.append(['ID', 'CUSTOMER_ID', 'OFFER_ID'])
        customer_offerData.append([i, random.randint(1, numOfCustomers+1), random.randint(1, numOfOffers+1)])
    return customer_offerData


def generateCustomer_ServiceData():
    customer_serviceData = []
    for i in range(1, numOfCustomerService + 1):
        # ID, CUSTOMER_ID, SERVICE_ID
        # append the header if i == 0
        if i == 1:
            customer_serviceData.append(['ID', 'CUSTOMER_ID', 'SERVICE_ID'])
        customer_serviceData.append([i, random.randint(1, numOfCustomers+1), random.randint(1, numOfServices+1)])
    return customer_serviceData


##############################################
# write data to csv file
def writeCSV(data, filename):
    with open(filename, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)
    csvFile.close()

# main function
def main():

    # department data generation must run before employee data generation.
    departmentData = generateDepartmentData()
    writeCSV(departmentData, "../CSVS/department.csv")
    employeeData = generateEmployeeData()
    writeCSV(employeeData, "../CSVS/employee.csv")
    customerData = generateCustomerData()
    writeCSV(customerData, "../CSVS/customer.csv")
    cardData = generateCardData()
    writeCSV(cardData, "../CSVS/card.csv")
    serviceData = generateServiceData()
    writeCSV(serviceData, "../CSVS/service.csv")
    complaintsData = generateCompliantsData()
    writeCSV(complaintsData, "../CSVS/complaints.csv")
    branchData = generateBranchData()
    writeCSV(branchData, "../CSVS/branch.csv")
    offerData = generateOfferData()
    writeCSV(offerData, "../CSVS/offer.csv")
    faqData = generateFAQData()
    writeCSV(faqData, "../CSVS/faq.csv")
    planData = generatePlanData()
    writeCSV(planData, "../CSVS/plan.csv")
    customer_offerData = generateCustomer_OfferData()
    writeCSV(customer_offerData, "../CSVS/customer_offer.csv")
    customer_serviceData = generateCustomer_ServiceData()
    writeCSV(customer_serviceData, "../CSVS/customer_service.csv")

if __name__ == "__main__":
    main()

