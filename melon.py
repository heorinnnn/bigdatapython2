import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 웹 드라이버 설정
chrome_options = Options()
chrome_options.add_argument('--headless')  # 창을 띄우지 않고 백그라운드에서 실행
chrome_options.add_argument('--disable-gpu')

# Chrome WebDriver 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 멜론 순위 페이지로 이동
url = "https://www.melon.com/chart/index.htm"
driver.get(url)

# 페이지가 완전히 로드될 때까지 잠시 대기
time.sleep(5)

# 100위까지의 곡 정보 가져오기
songs = []
for i in range(1, 101):  # 1위부터 100위까지
    try:
        rank = driver.find_element(By.XPATH, f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[2]/div/span').text  # 순위
        title = driver.find_element(By.XPATH, f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[3]/div/div/div/a').text  # 곡 제목
        artist = driver.find_element(By.XPATH, f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[4]/div/div/span/a').text  # 아티스트 이름
        
        songs.append({
            "순위": rank,
            "곡 제목": title,
            "아티스트": artist
        })
    except Exception as e:
        print(f"Error at rank {i}: {e}")

# 웹 드라이버 종료
driver.quit()

# DataFrame으로 저장
df = pd.DataFrame(songs)

# CSV 파일로 저장
df.to_csv('melon_top_100.csv', index=False, encoding='utf-8-sig')

# 출력
