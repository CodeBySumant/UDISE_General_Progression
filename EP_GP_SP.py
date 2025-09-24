# ==================== Ask user for Class at the very start ====================
try:
    selected_class = int(input("Enter the class of the student (1-10): "))
    if selected_class not in range(1, 11):
        raise ValueError("Class must be between 1 and 10.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default class 10.")
    selected_class = 10
# ==================== Ask user for Class at the very start ====================
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

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://sdms.udiseplus.gov.in/p0/v1/login?state-id=110")
driver.maximize_window()

input_element = driver.find_element(By.CLASS_NAME, "form-control")
input_element.send_keys("")

input_element = driver.find_element(By.ID, "password-field")
input_element.send_keys("")
time.sleep(15)

try:
    login_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "submit-btn"))
    )
    login_button.click()
except Exception as e:
    print(f"Error clicking login button: {e}")
time.sleep(25)

student_count = 1
while True:

###General Profile__Start

    print(f"Processing student #{student_count}")

## Drop down to bottom of page

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    
    # Fills up the blood group (only if empty)
    try:
        blood_group_select = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "select[formcontrolname='bloodGroup']"))
        ))

        # Check if a value is already selected
        if blood_group_select.first_selected_option.get_attribute("value") == "":
            blood_group_select.select_by_value("9")
    except Exception as e:
        print(f'Error while selecting blood group: {e}')

## click save for general profile

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space(span/text())='Save']"))
    ).click()
    time.sleep(1)

## close buttom after clicking save

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.swal2-actions > button.swal2-confirm"))
    ).click()
    time.sleep(1)

## next button after clicking close

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="button" and @matsteppernext]'))
    ).click()
    time.sleep(1)

###General Profile__Ends

###Enrolment Profile_Starts
    # drop down to submission
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    ## click save for Enrolment Profile
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[2]/form/div/app-enrolment-edit-new-ac/div/div/div/form/div[2]/div/button[2]'))
    ).click()
    time.sleep(1)

    ## Click Next after clicking save
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "swal2-cancel"))
    ).click()
    time.sleep(1)

###Enrolment Profile_ends

### Facility Profile_starts
    # 4.3.1 Whether Facilities provided to the Student (for the year of filling data)?
    # For YES & Free TextBook
    try:
        yes_radio = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @formcontrolname='facProvYN' and @value='1']"))
        )
        driver.execute_script("arguments[0].click();", yes_radio)
        time.sleep(1)

        # Click Free TextBook after selecting YES
        textbook_checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and @id='textbook']"))
        )
        textbook_checkbox.click()
        time.sleep(1)

    except Exception as e:
        print(f"Error clicking YES radio button: {e}")

    # click 4.3.3 Whether Student has been screened for Specific Learning Disability (SLD)?
    try:
        sld_radio = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @formcontrolname='screenedForSld' and @value='2']"))
        )
        driver.execute_script("arguments[0].click();", sld_radio)
        time.sleep(0.5)
    except Exception as e:
        print(f"Error clicking SLD radio button: {e}")

    # click 4.3.4 Whether Student has been screened for Autism Spectrum Disorder (ASD)?
    try:
        asd_radio = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @formcontrolname='autismSpectrumDisorder' and @value='2']"))
        )
        driver.execute_script("arguments[0].click();", asd_radio)
        time.sleep(0.5)
    except Exception as e:
        print(f"Error clicking ASD radio button: {e}")

    #4.3.5 Whether Student has been screened for Attention Deficit Hyperactive Disorder (ADHD)?
    try:
        adhd_radio = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @formcontrolname='attentionDeficitHyperactiveDisorder' and @value='2']"))
        )
        driver.execute_script("arguments[0].click();", adhd_radio)
        time.sleep(0.5)
    except Exception as e:
        print(f"Error clicking ADHD radio button: {e}")

    # click 4.3.6 Has the Student been identified as Gifted/Talented?
    try:
        gifted_radio = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @formcontrolname='giftedChildrenYn' and @value='2']"))
        )
        driver.execute_script("arguments[0].click();", gifted_radio)
        time.sleep(0.5)
    except Exception as e:
        print(f"Error clicking Gifted Children radio button: {e}")

    # click 4.3.7 State/National Competitions/Olympiads
    try:
        olympiads_radio = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @formcontrolname='olympdsNlc' and @value='2']"))
        )
        driver.execute_script("arguments[0].click();", olympiads_radio)
        time.sleep(0.5)
    except Exception as e:
        print(f"Error clicking Olympiads/NLC radio button: {e}")

    # click 4.3.8 Participation in NCC/NSS/Scouts & Guides
    try:
        ncc_radio = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @formcontrolname='nccNssYn' and @value='2']"))
        )
        driver.execute_script("arguments[0].click();", ncc_radio)
        time.sleep(0.5)
    except Exception as e:
        print(f"Error clicking NCC/NSS radio button: {e}")

    # click 4.3.9 Capable of handling digital devices including internet
    # For YES
    # try:
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[3]/form/div/app-other-details-edit-new-ac/div/div/div/form/div[1]/div/div/div[2]/div[3]/span/div[1]/input'))
    #     ).click()
    # except Exception as e:
    #     print(f"Error clicking Digital Devices checkbox: {e}")
    
    # For NO
    try:
        WebDriverWait(driver, 10).until(
            # EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div[3]/div/div/div/form/div/app-other-details-edit-new-ac/div/div/div/form/div[1]/div/div/div[2]/div[3]/span/div[2]/input'))
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='DGC'][value='2']"))
        ).click()
    except Exception as e:
        print(f"Error clicking Digital Devices checkbox: {e}")


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
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[3]/form/div/app-other-details-edit-new-ac/div/div/div/form/div[2]/div/button[2]'))
    ).click()
    time.sleep(1)

    #click next after clicking Save for Facility Profile
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Next')]"))
    ).click()
    time.sleep(1)


###Facility Profile_ends

###Profile Preview_starts

    # drop down to submission
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    #click on Complete Data
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-edit-student-new-ac/div/div/div/div/div[2]/div/mat-stepper/div/div[2]/div[4]/div/app-preview-new-ac/form/div/div[3]/div[3]/div/button[3]'))
    ).click()
    time.sleep(1)

    # # click Okay button

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="button" and contains(@class, "swal2-cancel")]'))
    ).click()
    time.sleep(2)
    
    # #click next student 

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="button" and contains(text(), "Next Student")]'))
    ).click()
    time.sleep(2)

###Profile Preview_Ends
    student_count += 1
