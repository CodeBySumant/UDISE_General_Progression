import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


def generate_random_integer(start, end):
    return str(random.randint(start, end))

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://sdms.udiseplus.gov.in/p0/v1/login?state-id=110")
driver.maximize_window()

input_element = driver.find_element(By.CLASS_NAME, "form-control")
input_element.send_keys("10140802109")

input_element = driver.find_element(By.ID, "password-field")
input_element.send_keys("Sstar@123")
time.sleep(15)

login_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.ID, "submit-btn"))
)
login_button.click()
time.sleep(1)

time.sleep(25)

student_count = 1
while True:

###General Profile__Start

    print(f"Processing student #{student_count}")

## Student Mobile Number

    first_digit = str(random.choice([6, 7, 8, 9]))
    remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(9))
    random_10_digit = first_digit + remaining_digits

    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='primaryMobile']"))
    )
    input_box.clear()
    input_box.send_keys(random_10_digit)

## Drop down to bottom of page

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

## blood group 

    blood_group_select = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//select[@formcontrolname="bloodGroup"]'))
    ))
    blood_group_select.select_by_value("9")
    time.sleep(1)

## click save for general profile

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(span/text())='Save']"))
    ).click()
    time.sleep(1)

## close buttom after clicking save

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.swal2-actions > button.swal2-confirm"))
    ).click()
    time.sleep(1)

## next button after clicking close

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="button" and @matsteppernext]'))
    ).click()
    time.sleep(1)

###General Profile__Ends

###Enrolment Profile_Starts

    # drop down to submission
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # click 4.2.6	(a) Whether Admitted under Section 12C of RTE Act? "NO"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[2]/form/div/app-enrolment-edit-new-ac/div/div/div/form/div[1]/div/div/div[10]/div/div[2]/div[2]/input'))
    ).click()
    time.sleep(1)

    ## click save for Enrolment Profile

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[2]/form/div/app-enrolment-edit-new-ac/div/div/div/form/div[2]/div/button[2]'))
    ).click()
    time.sleep(1)

    ## Click Next after clicking save

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "swal2-cancel"))
    ).click()
    time.sleep(1)

###Enrolment Profile_ends

###Facility Profile_starts

    # click 4.3.3 Whether Student has been screened for Specific Learning Disability (SLD)?
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[3]/form/div/app-other-details-edit-new-ac/div/div/div/form/div[1]/div/div/div[1]/div[1]/span[1]/div[2]/input'))
    ).click()
    time.sleep(1)

    #click 4.3.4 Whether Student has been screened for Autism Spectrum Disorder (ASD)?
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[3]/form/div/app-other-details-edit-new-ac/div/div/div/form/div[1]/div/div/div[1]/div[2]/span/div[2]/input'))
    ).click()
    time.sleep(1)

    #click 4.3.5 Whether Student has been screened for Attention Deficit Hyperactive Disorder (ADHD)?
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[3]/form/div/app-other-details-edit-new-ac/div/div/div/form/div[1]/div/div/div[1]/div[3]/span/div[2]/input'))
    ).click()
    time.sleep(1)

    #click 4.3.6 as the Student been identified as a Gifted / Talented?
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[3]/form/div/app-other-details-edit-new-ac/div/div/div/form/div[1]/div/div/div[1]/div[4]/span/div[2]/input'))
    ).click()
    time.sleep(1)

    #click 4.3.7 Does the student appeared in any State Level Competitions/ National level Competitions/ Olympiads?
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[3]/form/div/app-other-details-edit-new-ac/div/div/div/form/div[1]/div/div/div[2]/div[1]/span/div[2]/input'))
    ).click()
    time.sleep(1)

    #click 4.3.8 Does the Student participate in NCC/ NSS/ Scouts and Guides?
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[3]/form/div/app-other-details-edit-new-ac/div/div/div/form/div[1]/div/div/div[2]/div[2]/span/div[2]/input'))
    ).click()
    time.sleep(1)

    #click 4.3.9 Whether student is capable of handling digital devices including the internet?
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[3]/form/div/app-other-details-edit-new-ac/div/div/div/form/div[1]/div/div/div[2]/div[3]/span/div[1]/input'))
    ).click()
    time.sleep(1)

# Height (cm) and Weight (kg) data for Class 1 to 10

    class_data = {
        1: {"height_cm": 115, "weight_kg": 21},
        2: {"height_cm": 122, "weight_kg": 23},
        3: {"height_cm": 128, "weight_kg": 26},
        4: {"height_cm": 133, "weight_kg": 29},
        5: {"height_cm": 138, "weight_kg": 32},
        6: {"height_cm": 144, "weight_kg": 36},
        7: {"height_cm": 149, "weight_kg": 40},
        8: {"height_cm": 156, "weight_kg": 45},
        9: {"height_cm": 164, "weight_kg": 51},
        10: {"height_cm": 170, "weight_kg": 56},
    }

    # choose Class student
    selected_class = 1

    # Base values
    base_height = class_data[selected_class]["height_cm"]
    base_weight = class_data[selected_class]["weight_kg"]

    # Generate random values within ±5
    student_height = str(random.randint(base_height - 5, base_height + 5))
    student_weight = str(random.randint(base_weight - 3, base_weight + 5))

    print(student_height)
    print(student_weight)

    # Dynamic XPaths (short & reliable using IDs)
    height_xpath = "//input[@id='height']"
    weight_xpath = "//input[@id='weight']"

    # Fill Height
    height_field = driver.find_element(By.XPATH, height_xpath)
    height_field.clear()
    height_field.send_keys(student_height)

    # Fill Weight
    weight_field = driver.find_element(By.XPATH, weight_xpath)
    weight_field.clear()
    weight_field.send_keys(student_weight)


    #click 4.3.11 Approximate Distance of student's residence to school
    distance_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//select[@formcontrolname="distanceFrmSchool"]'))
    )
    Select(distance_dropdown).select_by_value("2")
    time.sleep(1)

    #click 4.3.12 Completed Highest Education Level of Mother/Father/Legal Guardian
    parent_education_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//select[@formcontrolname="parentEducation"]'))
    )
    Select(parent_education_dropdown).select_by_value("5")
    time.sleep(1)

    # click save for Facility Profile
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[3]/form/div/app-other-details-edit-new-ac/div/div/div/form/div[2]/div/button[2]'))
    ).click()
    time.sleep(1)

    #click next after clicking Save for Facility Profile
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]"))
    ).click()
    time.sleep(1)


###Facility Profile_ends

###Profile Preview_starts

    # drop down to submission
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    #click on Complete Data
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[4]/div/app-preview-new-ac/form/div/div[3]/div[3]/div/button[3]'))
    ).click()
    time.sleep(2)

    # # click Okay
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Okay']"))
    # ).click()
    # time.sleep(2)

    # #click next student
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next Student']"))
    # ).click()
    # time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="button" and contains(@class, "swal2-cancel")]'))
    ).click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="button" and contains(text(), "Next Student")]'))
    ).click()
    time.sleep(2)
###Profile Preview_Ends
    student_count += 1
