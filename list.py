import random
import time

# 가상의 노래 리스트 생성 (1위부터 100위까지)
songs = [f"곡 {i} - 노래" for i in range(1, 101)]  # "곡 1 - 노래"부터 "곡 100 - 노래"

# 추천 시스템 출력
print("멜론 차트 1위부터 100위까지 추천해 드릴게요!")
print("")

# AI 추천 시작
print("AI야, 멜론 차트 1위부터 100위까지 추천해줘!")
print("""
알겠습니다. 
제가 열심히 분석해서 
고객님께 차트 순위에 맞는 노래를 
추천해드립니다.
""")

# AI가 추천하는 과정 (간단한 랜덤화)
random_song = random.choice(songs)

# 추천과정 출력 (두둥 두둥~)
dd = ["두", "두", "두", "두둥"]
for d in dd:
    print(d)
    time.sleep(1)

# 최종 추천
print(f"제가 추천한 곡은 바로: {random_song}입니다.")

# 차트에서 1위부터 10위까지 보여주는 예시
print("\n차트 1위부터 10위까지의 곡을 살펴볼까요?")
for i in range(10):
    print(f"{i+1}위: {songs[i]}")

# 원하는 차트를 더 많은 순위까지 추천하려면 다음과 같이 확장 가능
# 예시: 1위부터 20위까지 추천
print("\n추가 추천 11위부터 20위까지:")
for i in range(10, 20):
    print(f"{i+1}위: {songs[i]}")
