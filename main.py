from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
browser.get('https://www.saucedemo.com/')

username_input = browser.find_element(By.ID, "user-name")
username_input.send_keys("standard_user")

password_input = browser.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = browser.find_element(By.ID, "login-button")
login_button.click()

product_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
assert product_title.is_displayed()
assert product_title.text == "PRODUCTS"

menu_button = browser.find_element(By.CSS_SELECTOR, "#react-burger-menu-btn")
menu_button.click()

logout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logout_sidebar_link")))
logout_button.click()

login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
assert login_button.is_displayed()

username_input = browser.find_element(By.ID, "user-name")
username_input.send_keys("locked_out_user")

password_input = browser.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = browser.find_element(By.ID, "login-button")
login_button.click()

error_box = wait.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".error-message-container"),
        "Epic sadface: Sorry, this user has been locked out.")
)
print(error_box)

browser.quit()
