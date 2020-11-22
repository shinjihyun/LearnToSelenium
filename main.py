
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
path = "C:/Users/skswl/bin/chromedriver.exe"
driver: WebDriver = webdriver.Chrome(path)

#로그인 페이지로 이동
driver.get('https://web-v2-dev.realclass.co.kr/new/account/login')
driver.implicitly_wait(5)

driver.find_element_by_name('accountName').send_keys('qa4@qualson.com')
driver.find_element_by_name('password').send_keys('11111111')

driver.implicitly_wait(5)

#로그인 버튼 누르기

driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div/form/button').send_keys(Keys.ENTER)
driver.implicitly_wait(5)

#프로필 버튼 누르기

notFound = True
while notFound:

    try:
        driver.implicitly_wait(4)
        driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div/div/div[1]/img').click()
        notFound = False
    except Exception as e:
        print(e)
        notFound = True






