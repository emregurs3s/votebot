from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# SIGN IN 'i fonksiyon haline getir.

driver = webdriver.Chrome()
def sign_in(driver):
    driver.get("https://www.nba.com/account/sign-in") 
    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )   
    time.sleep(3)
    email = driver.find_element(By.XPATH,"//*[@id='email']")
    password = driver.find_element(By.XPATH,"//*[@id='password']")  
    
    email.send_keys("email")
    password.send_keys("password")  

    enter = driver.find_element(By.XPATH,"//*[@id='submit']")
    cookies = driver.find_element(By.XPATH,"//*[@id='onetrust-accept-btn-handler']")
    
    cookies.click()
    time.sleep(3)
    enter.click()   
    time.sleep(20)
sign_in(driver)

driver.quit()
