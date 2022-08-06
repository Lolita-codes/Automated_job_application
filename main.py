import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import os

ACCOUNT_EMAIL = os.environ['ACCOUNT_EMAIL']
ACCOUNT_PASSWORD = os.environ['ACCOUNT_PASSWORD']
PHONE_NUMBER = os.environ['PHONE_NUMBER']
CHROME_DRIVER_PATH = os.environ['CHROME_DRIVER_PATH']

chrome_driver_path = CHROME_DRIVER_PATH
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Searching for python developer jobs in Lagos, Nigeria
driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=104197452&keywords=python%20developer&location=Lagos%2C%20Nigeria')

#  Automatically log in to LinkedIn, sleep() to wait for pages to fully load
time.sleep(3)
sign_in = driver.find_element(By.CSS_SELECTOR, ' div a.nav__button-secondary.btn-md.btn-secondary-emphasis')
sign_in.click()
time.sleep(5)
email = driver.find_element(By.CSS_SELECTOR, '#username')
email.send_keys(ACCOUNT_EMAIL)
time.sleep(5)
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(ACCOUNT_PASSWORD)
time.sleep(5)
log_in = driver.find_element(By.CSS_SELECTOR, 'div.login__form_action_container button')
log_in.click()
time.sleep(10)

#  Apply to all the jobs on the page
jobs = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')
for job in jobs:
    print('found')
    time.sleep(5)
    job.click()
    print('clicked')
    time.sleep(5)

    # Automatically apply to the first job that requires to enter only phone number.
    try:
        apply = driver.find_element(By.CLASS_NAME, 'jobs-apply-button').click()
        time.sleep(5)

        phone_box = driver.find_element(By.CLASS_NAME, 'fb-single-line-text')
        time.sleep(5)
        if phone_box == '':
            phone_box.send_keys(PHONE_NUMBER)
            time.sleep(5)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        #  Ignores the applications that require a note and the complex, multi-step applications
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss').click()
            time.sleep(5)

            discard_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn')[1].click()
            print('Complex process, application skipped.')
            continue
        else:
            submit_button.click()

        time.sleep(5)
        close_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss').click()

    # When the element cannot be found
    except NoSuchElementException:
        print("No application button, process skipped.")
        continue

time.sleep(5)
driver.quit()





