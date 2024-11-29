from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os


class WebAutomation:
    def __init__(self):

        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-chocie-screen")

        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service("chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)
        

    def login(self, username, passw):
        self.driver.get("https://demoqa.com/login")
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        # login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))
        login_button = self.driver.find_element(By.ID, "login")

        username_field.send_keys(username)
        password_field.send_keys(passw)
        self.driver.execute_script("arguments[0].click();", login_button)


    def fill_form(self, name, email, cur_address, address):
        # Locate the Element dropdown and Textbox 
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))

        elements.click()

        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="item-0"]')))
        text_box.click()

        # Locate the form fields and submit button
        full_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')


        # Fill in the from Fields
        full_name_field.send_keys(name)
        email_field.send_keys(email)
        current_address_field.send_keys(cur_address)
        permanent_address_field.send_keys(address)
        self.driver.execute_script("arguments[0].click();", submit_button)
    

    def download(self):
        # Get download section and click on it 
        download_section = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        download_section.click()

        # Get download button and click on it 

        download_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "downloadButton")))
        download_button.click()


    def close(self):
        self.driver.quit()



if __name__ == "__main__":
    load_dotenv()
    username = os.getenv("APPUSERNAME")
    passw = os.getenv("PASS")

    webautomation= WebAutomation()
    webautomation.login(username, passw)
    webautomation.fill_form("John Smith", "johnsmith@example.com", "John Street 100 New York USA", "John Street 100 New York USA"  )
    webautomation.download()
    input()
    webautomation.close()