from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

accounts = {"E-Mail": "password",
            "E-Mail2": "password2"}

def login(gmailId, passWord):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
        'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
        '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        driver.implicitly_wait(15)
    
        loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
        loginBox.send_keys(gmailId)
    
        nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
        nextButton[0].click()
    
        passWordBox = driver.find_element_by_xpath(
            '//*[@id ="password"]/div[1]/div / div[1]/input')
        passWordBox.send_keys(passWord)
    
        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        nextButton[0].click()
    
        print('Login Successful...!!')
        time.sleep(10)
        driver.quit()

    except:
        print('Login Failed')


for account, password in accounts.items():
    login(account, password)
