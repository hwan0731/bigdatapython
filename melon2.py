# 1. 멜론 100곡 출력 
# 2. 멜론 50곡 출력 
# 3. 멜론 10곡 출력 
# 4. AI 추천곡 출력 
# 5. 가수 이름 검색 
print("=================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("=================")
# 메뉴선택(숫자입력): 1
n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n} ")
# 여기까지는 n이 문자열 
# n = int(n) # 숫자로 변경(연산을 해야 된다면)
# 여기서 부터는 n은 숫자(정수) 


# 만약에 1을 입력하면
# 멜론 100 출력
if n == "1":
    print("멜론 100")
# else: 
    print("1이 아닙니다.")
# 만약에 2를 입력하면 
# 멜론 50 출력 
elif n == "2":
    print("멜론 50")
# ... 
# 5를 입력하면 가수 이름 검색할 수 있게 입력창이 또 나와야함 
# 이름을 입력하면 해당 가수 이름의 노래 리스트가 출력
else: 
    print("1~5까지 입력하세요")


print("=================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("=================")

n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n} ")
# 여기까지는 n이 문자열 
# n = int(n) # 숫자로 변경(연산을 해야 된다면)
# 여기서 부터는 n은 숫자(정수) 

# 멜론 차트 데이터 (예시)
def get_melon_chart(count):
    """멜론 차트 데이터를 반환하는 함수"""
    melon_data = [
        {"rank": 1, "title": "Perfect Night", "artist": "르세라핌"},
        {"rank": 2, "title": "Baddie", "artist": "IVE"},
        {"rank": 3, "title": "Seven (feat. Latto)", "artist": "정국"},
        {"rank": 4, "title": "너의 모든 순간", "artist": "성시경"},
        {"rank": 5, "title": "에잇", "artist": "아이유"},
        {"rank": 6, "title": "Love Lee", "artist": "AKMU"},
        {"rank": 7, "title": "사건의 지평선", "artist": "윤하"},
        {"rank": 8, "title": "Super Shy", "artist": "NewJeans"},
        {"rank": 9, "title": "Hype Boy", "artist": "NewJeans"},
        {"rank": 10, "title": "Ditto", "artist": "NewJeans"},
        # 추가 곡들
        {"rank": 11, "title": "I AM", "artist": "IVE"},
        {"rank": 12, "title": "OMG", "artist": "NewJeans"},
        {"rank": 13, "title": "Dynamite", "artist": "방탄소년단"},
        {"rank": 14, "title": "Cupid", "artist": "FIFTY FIFTY"},
        {"rank": 15, "title": "어떻게 이별까지 사랑하겠어", "artist": "AKMU"},
        {"rank": 16, "title": "사랑은 늘 도망가", "artist": "임영웅"},
        {"rank": 17, "title": "Butter", "artist": "방탄소년단"},
        {"rank": 18, "title": "봄날", "artist": "방탄소년단"},
        {"rank": 19, "title": "Smoke", "artist": "다이나믹 듀오"},
        {"rank": 20, "title": "ASAP", "artist": "STAYC"},
    ]
    
    # 더 많은 곡이 필요하면 생성
    if count > len(melon_data):
        for i in range(len(melon_data)+1, count+1):
            melon_data.append({"rank": i, "title": f"노래 제목 {i}", "artist": f"가수 {i}"})
    
    return melon_data[:count]

# AI 추천 노래 데이터 (예시)
def get_ai_recommendations():
    """AI 추천 노래 목록을 반환하는 함수"""
    return [
        {"title": "꽃", "artist": "지코", "reason": "최근 들은 곡과 비슷한 분위기"},
        {"title": "사랑하지 않아서 그랬어", "artist": "황인욱", "reason": "사용자 취향 기반 추천"},
        {"title": "신호등", "artist": "이무진", "reason": "인기 급상승 중인 곡"},
        {"title": "맞네", "artist": "중첩", "reason": "사용자와 비슷한 취향의 다른 유저들이 선호"},
        {"title": "After Like", "artist": "IVE", "reason": "최근 들은 아티스트의 다른 인기곡"}
    ]

# 가수별 노래 목록 검색 함수
def search_artist(artist_name):
    """가수 이름으로 노래 목록을 검색하는 함수"""
    # 모든 멜론 데이터에서 검색 (100곡)
    songs = get_melon_chart(100)
    result = []
    
    for song in songs:
        if artist_name.lower() in song["artist"].lower():
            result.append(song)
    
    return result

# 만약에 1을 입력하면 멜론 100 출력
if n == "1":
    print("\n멜론 TOP 100")
    print("=====================================")
    songs = get_melon_chart(100)
    for song in songs:
        print(f"{song['rank']:3d}. {song['title']} - {song['artist']}")
    print("=====================================")

# 만약에 2를 입력하면 멜론 50 출력
elif n == "2":
    print("\n멜론 TOP 50")
    print("=====================================")
    songs = get_melon_chart(50)
    for song in songs:
        print(f"{song['rank']:3d}. {song['title']} - {song['artist']}")
    print("=====================================")

# 만약에 3을 입력하면 멜론 10 출력
elif n == "3":
    print("\n멜론 TOP 10")
    print("=====================================")
    songs = get_melon_chart(10)
    for song in songs:
        print(f"{song['rank']:3d}. {song['title']} - {song['artist']}")
    print("=====================================")

# 만약에 4를 입력하면 AI 추천 노래 출력
elif n == "4":
    print("\nAI 추천 노래")
    print("=====================================")
    recommendations = get_ai_recommendations()
    for i, song in enumerate(recommendations, 1):
        print(f"{i}. {song['title']} - {song['artist']}")
        print(f"   추천 이유: {song['reason']}")
    print("=====================================")

# 만약에 5를 입력하면 가수 이름 검색
elif n == "5":
    artist_name = input("\n검색할 가수 이름을 입력하세요: ")
    result = search_artist(artist_name)
    
    print(f"\n'{artist_name}' 검색 결과")
    print("=====================================")
    
    if result:
        for song in result:
            print(f"{song['rank']:3d}. {song['title']} - {song['artist']}")
    else:
        print(f"'{artist_name}'의 노래를 찾을 수 없습니다.")
    
    print("=====================================")

# 1~5 이외의 입력에 대한 처리
else:
    print("1~5까지 입력하세요")

