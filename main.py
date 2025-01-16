from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def solve_captcha(driver):
    try:
        
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, "//iframe[starts-with(@name, 'a-') and contains(@src, 'recaptcha')]")
            )
        )
       
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-border"))
        ).click()
        print("Captcha çözüldü.")
        driver.switch_to.default_content()
        time.sleep(2)
    except Exception as e:
        print(f"Captcha bulunamadı veya çözülemedi: {e}")

def sign_in(driver):
    driver.get("https://www.nba.com/account/sign-in") 
    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )   
    time.sleep(3)
    email = driver.find_element(By.XPATH,"//*[@id='email']")
    password = driver.find_element(By.XPATH,"//*[@id='password']")  
    
    email.send_keys("emregurses06@gmail.com")
    password.send_keys("Jokerfurkan1")  

    enter = driver.find_element(By.XPATH,"//*[@id='submit']")
    cookies = driver.find_element(By.XPATH,"//*[@id='onetrust-accept-btn-handler']")
    
    cookies.click()
    time.sleep(3)
    enter.click()   
    time.sleep(3)
    solve_captcha(driver)


def vote(driver):
    time.sleep(5)
    
    allstar = driver.find_element(By.XPATH,"//*[@id='nav-ul']/li[5]/a")
    allstar.click()
    time.sleep(5)
    votelink = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div[2]/main/div[3]/section/div/div[2]/div[1]/a")
    votelink.click()
    time.sleep(5)
    screenclick = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[5]/div/div/div/div")
    screenclick.click()
    time.sleep(15)
    search = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]/div/a")
    search.send_keys("ALPEREN SENGUN")
    time.sleep(2)
    plusbtn = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]/section[2]/div[2]/div[1]/div/div/div[1]/div/button")
    plusbtn.click()
    time.sleep(2)
    reviewbtn = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[4]/div[1]/button")
    reviewbtn.click()
    time.sleep(2)
    submitbtn = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[4]/div[1]/button")
    submitbtn.click()

sign_in(driver)
vote(driver)

driver.quit()
