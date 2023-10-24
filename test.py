from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

# Set the path to your web driver (e.g., chromedriver or geckodriver)
SELENIUM_CHROME_BINARY= str(os.getenv('SELENIUM_CHROME_BINARY')) # Prevent TypeError: Binary Location Must be a String
SELENIUM_CHROME_DRIVER= os.getenv('SELENIUM_CHROME_DRIVER')

options = webdriver.ChromeOptions()
options.binary_location = SELENIUM_CHROME_BINARY
options.add_argument('--headless')
service = Service(SELENIUM_CHROME_DRIVER)
driver = webdriver.Chrome(service=service, options=options)

# Open the Flask app in your local development server
app_url = 'http://127.0.0.1:5000'  # Replace with your Flask app URL
driver.get(app_url)

# Find the input element and submit button
input_element = driver.find_element(By.NAME, 'name')
submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

# Enter a name in the input field
test_name = 'Yusuf'  # Replace with the name you want to test
input_element.send_keys(test_name)

# Submit the form
submit_button.click()

# Wait for a moment to allow the page to load
time.sleep(2)

# Verify that the result page contains the entered name
result_text = driver.find_element(By.TAG_NAME, 'p').text
expected_result = test_name

if result_text == expected_result:
    print(f'Test passed: Name "{test_name}" was submitted successfully.')
else:
    print(f'Test failed: Name "{test_name}" was not found on the result page.')

# Close the browser
driver.quit()