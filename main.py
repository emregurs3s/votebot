from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
def captcha_manuel_solve():
    input("Please , solve the captcha and press enter.")

def sign_in(driver):
    driver.get("https://www.nba.com/account/sign-in")
    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    time.sleep(3)
    email = driver.find_element(By.XPATH,"//*[@id='email']")
    password = driver.find_element(By.XPATH,"//*[@id='password']")  
    
    email.send_keys("username")
    password.send_keys("password")  

    enter = driver.find_element(By.XPATH,"//*[@id='submit']")
    cookies = driver.find_element(By.XPATH,"//*[@id='onetrust-accept-btn-handler']")
    
    cookies.click()
    time.sleep(3)
    enter.click()
    time.sleep(5)
    captcha_manuel_solve()
    driver.get("https://vote.nba.com/en")

def vote(driver):
    driver.get("https://vote.nba.com/en/search")
    search = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/section[1]/div/input')  
    search.send_keys("ALPEREN SENGUN")
    time.sleep(5)
    plusbtn = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]/section[2]/div[2]/div[1]/div/div/div[1]/div/button")
    plusbtn.click()
    time.sleep(5)
    reviewbtn = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[4]/div[1]/button")
    reviewbtn.click()
    time.sleep(5)
    submitbtn = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[4]/div[1]/button")
    submitbtn.click()
    time.sleep(2)
    captcha_manuel_solve()
    time.sleep(5)
    submitvote = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[5]/div/div/div/div/div[3]/button")
    submitvote.click()

    time.sleep(10)

sign_in(driver)
vote(driver)

driver.quit()
