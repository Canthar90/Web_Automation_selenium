from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os



load_dotenv()
username = os.getenv("APPUSERNAME")
passw = os.getenv("PASS")

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-chocie-screen")


service = Service("chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get("https://demoqa.com/login")


username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))


username_field.send_keys(username)
password_field.send_keys(passw)
login_button.click()


input("Press enter to close the browser")
driver.quit()