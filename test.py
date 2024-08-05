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
driver.get("https://naver.com")

# 페이지 요소 찾기 및 동작 수행
# 예: 검색창에 텍스트 입력 후 엔터키 누르기
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python 웹 매크로")
search_box.send_keys(Keys.RETURN)

# 몇 초 대기 (페이지 로딩 대기)
time.sleep(3)

# 다른 동작 수행 예: 첫 번째 검색 결과 클릭
first_result = driver.find_element(By.CSS_SELECTOR, "h3 > a")
first_result.click()

# 몇 초 대기
time.sleep(3)

# 브라우저 닫기
driver.quit()