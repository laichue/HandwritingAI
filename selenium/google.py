from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl")#구글 이미지 검색 초기 창 주소
elem = driver.find_element(By.NAME, "q")#구굴창에서 검색창 위치(?)값 선택
elem.send_keys("푸른 해파리")#검색창에 검색어 입력
elem.send_keys(Keys.RETURN)#엔터키

#검색 결과로 나온 이미지 하나식 저장하기
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")#각 작은 이미지들 리스트(?)에 저장
count = 1
for image in images:
	image.click()#각 이미지 저장
	time.sleep(3)
	imgUrl = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".n3VNCb"))).get_attribute("src")#이미지 주소 획득
	urllib.request.urlretrieve(imgUrl, str(count)+".jpg")#해당 주소에 있는 이미지 저장
	count = count + 1
 
while(True):#열린 창 바로 닫힘 문제 해결: while문을 지속 수행해 함수가 종료되지 않게하여 selenium제어창을 유지
    	pass