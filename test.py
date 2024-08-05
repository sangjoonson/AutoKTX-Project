# you need to install selenium, webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 웹드라이버 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 웹 페이지 열기
driver.get("https://etk.srail.co.kr/cmc/01/selectLoginForm.do")

driver.implicitly_wait(15) # 페이지 다 뜰 때 까지 기다림

driver.find_element(By.ID, 'srchDvNm01').send_keys('12345677234') # 회원번호
driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys("1111111111") # 비밀번호

driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
driver.implicitly_wait(5)