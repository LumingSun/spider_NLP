from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def log_in():
    website = r'https://www.alexa.com/login'
    path = r"d:\python\chromedriver\chromedriver.exe"
    path = r'd:\python\phantomjs\bin\phantomjs.exe'
    browser = webdriver.PhantomJS(path)
    browser.get(website)
    email = browser.find_element(By.ID,'email')
    email.send_keys('luming_s@126.com')
    pwd = browser.find_element(By.ID,'pwd')
    pwd.send_keys('Mp_i9(@@')
    submit = browser.find_element(By.ID,'submit')
    submit.submit()
    print("log in")
    for web in ['www.youku.com','baidu.com']:
        searchplace = browser.find_element(By.CLASS_NAME, 'searchtext')
        searchplace.send_keys(web)
        searchplace.submit()
        globalRank = browser.find_element(By.CLASS_NAME, 'globleRank').text.lstrip("Global Rank").lstrip()
        print(globalRank)
        countryRank = browser.find_element(By.CLASS_NAME, 'countryRank').text.lstrip("Rank in ").lstrip().replace(
            "\n\n\n\n\n\n", " ")
        print(countryRank)
    browser.close()


def spider_chrome(browser,website):
    globalRank = browser.find_element(By.CLASS_NAME, 'globleRank').text.lstrip("Global Rank").lstrip()
    print(globalRank)
    countryRank = browser.find_element(By.CLASS_NAME, 'countryRank').text.lstrip("Rank in ").lstrip().replace("\n\n\n\n\n\n", " ")
    print(countryRank)

log_in()
