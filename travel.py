import pandas as pd  # pandas는 데이터 처리와 CSV 파일 저장을 위한 라이브러리

# 20대들이 가장 좋아하는 해외 여행지 10개 리스트
top_10_travel_destinations = [
    "일본",
    "베트남",
    "태국",
    "대만",
    "홍콩",
    "필리핀",
    "인도네시아",
    "에스토니아",
    "터키",
    "슬로베니아"
]

# 순위 출력
print("20대들이 가장 좋아하는 해외 여행지 Top 10:")
for idx, country in enumerate(top_10_travel_destinations, start=1):
    print(f"{idx}. {country}")

# 데이터를 pandas DataFrame으로 변환
df = pd.DataFrame({
    "순위": range(1, 11),  # 순위를 1부터 시작하도록 설정
    "여행지": top_10_travel_destinations
})

# 데이터를 CSV 파일로 저장
df.to_csv("top_10_travel_destinations.csv", index=False, encoding="utf-8-sig")

print("\n데이터가 'top_10_travel_destinations.csv' 파일로 저장되었습니다!")