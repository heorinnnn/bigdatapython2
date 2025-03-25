import requests
from bs4 import BeautifulSoup

# 멜론 100위 페이지 URL
url = "https://www.melon.com/chart/index.htm"

# 헤더 설정 (서버가 봇을 차단하지 않도록 user-agent를 설정)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 요청 보내기
response = requests.get(url, headers=headers)

# 응답이 성공적이면
if response.status_code == 200:
    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 순위 데이터 추출
    chart_items = soup.find_all('tr', {'class': 'lst50'})  # lst50은 멜론 차트 항목 클래스
    
    # 100위까지 순위 출력
    for rank, item in enumerate(chart_items, start=1):
        if rank > 100:
            break
        song_title = item.find('div', {'class': 'ellipsis'}).text.strip()
        artist_name = item.find('span', {'class': 'checkEllipsis'}).text.strip()
        print(f"{rank}위: {song_title} - {artist_name}")
else:
    print(f"요청 실패: {response.status_code}")