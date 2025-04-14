print("안녕 루피야")



def m100(a):
    print(a)
    time.sleep(1)
    if response. status_code == 200:
        soup = Beautifulsoup(response.tsxt, 'html.parser')

        songs = soup.select('tr[data-song-no]')

        for index, song in enu,erate(songs):
            if index >= 100:
                break 
            rank = song.select_one('div.ellipsis.rank01 a'). text. strip()

import requests
from bs4 import BeautifulSoup
import random
import time 

def m100(a):
    print(a)
    time. sleep(1)

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

# 수집한 데이터를 출력합니다. 
for song in songs:
    print(f"{song[0]}. {song[1]} - {song[2]}")

    # 헤더 설정 (멜론은 User-Agent 확인을 통해 봇 접근을 차단할 수 있으므로 설정이 필요할 수 있음)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 웹페이지 요청
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 노래 제목과 아티스트를 담을 리스트
songs = []

# 멜론 차트의 노래 제목과 아티스트를 찾습니다.
#lst50 #frm > div > table > tbody #lst50
for entry in soup.select('tr.lst50, tr.lst100'):  # 상위 50위 및 100위 목록
    rank = entry.select_one('span.rank').get_text()
    title = entry.select_one('div.ellipsis.rank01 a').get_text()
    artist = entry.select_one('div.ellipsis.rank02 a').get_text()
    songs.append((rank, title, artist))

# 수집한 데이터를 출력합니다.
for song in songs:
    print(f"{song[0]}. {song[1]} - {song[2]}")


    # 1. 멜론 100곡 출력
# 2. 멜론 50곡 출력
# 3. 멜론 10곡 출력
# 4. AI 추천곡 출력
# 5. 가수 이름 검색

# 간단한 음악 메뉴 프로그램

def show_menu():
    """메뉴를 출력하는 함수"""
    print("=================")
    print("1. 멜론 100")
    print("2. 멜론 50")
    print("3. 멜론 10")
    print("4. AI 추천 노래")
    print("5. 가수 이름 검색")
    print("0. 종료")
    print("=================")

def process_menu():
    """사용자 입력을 처리하는 함수"""
    while True:
        show_menu()
        choice = input("메뉴선택(숫자입력): ")
        
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            print("멜론 100곡을 출력합니다.")
            # 여기에 멜론 100곡 출력 코드 추가
        elif choice == "2":
            print("멜론 50곡을 출력합니다.")
            # 여기에 멜론 50곡 출력 코드 추가
        elif choice == "3":
            print("멜론 10곡을 출력합니다.")
            # 여기에 멜론 10곡 출력 코드 추가
        elif choice == "4":
            print("AI 추천 노래를 출력합니다.")
            # 여기에 AI 추천 노래 출력 코드 추가
        elif choice == "5":
            artist = input("검색할 가수 이름을 입력하세요: ")
            print(f"{artist}의 노래를 검색합니다.")
            # 여기에 가수 검색 코드 추가
        else:
            print("0~5 사이의 숫자를 입력해주세요.")
        
        print("\n")  # 메뉴 사이 빈 줄 추가

# 프로그램 실행
if __name__ == "__main__":
    print("음악 차트 프로그램을 시작합니다.")
    process_menu()

# 간단한 음악 메뉴 프로그램

def show_menu():
    """메뉴를 출력하는 함수"""
    print("=================")
    print("1. 멜론 100")
    print("2. 멜론 50")
    print("3. 멜론 10")
    print("4. AI 추천 노래")
    print("5. 가수 이름 검색")
    print("0. 종료")
    print("=================")

def process_menu():
    """사용자 입력을 처리하는 함수"""
    while True:
        show_menu()
        choice = input("메뉴선택(숫자입력): ")
        
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            print("멜론 100곡을 출력합니다.")
            # 여기에 멜론 100곡 출력 코드 추가
        elif choice == "2":
            print("멜론 50곡을 출력합니다.")
            # 여기에 멜론 50곡 출력 코드 추가
        elif choice == "3":
            print("멜론 10곡을 출력합니다.")
            # 여기에 멜론 10곡 출력 코드 추가
        elif choice == "4":
            print("AI 추천 노래를 출력합니다.")
            # 여기에 AI 추천 노래 출력 코드 추가
        elif choice == "5":
            artist = input("검색할 가수 이름을 입력하세요: ")
            print(f"{artist}의 노래를 검색합니다.")
            # 여기에 가수 검색 코드 추가
        else:
            print("0~5 사이의 숫자를 입력해주세요.")
        
        print("\n")  # 메뉴 사이 빈 줄 추가

# 프로그램 실행
if __name__ == "__main__":
    print("음악 차트 프로그램을 시작합니다.")
    process_menu()

def m_random():
    print(d)
    time.sleep

    import requests
from bs4 import BeautifulSoup
import random
import time

def m000(a, c):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= c:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')

def m100(a):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 100:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')

def m50(a):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 50:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')

def m10(a):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 10:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')


def m000(a, c):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= c:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')

def m_random(d):
    print(d)
    time.sleep(1)
    print("[좋아요! 제가 열심히 찾아서 사용자님께 노래를 한 곡 추천할게요.]")
    time.sleep(1)
    print(f"[두구두구둥...]")
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        songs = soup.select('tr[data-song-no]')
        song_list = []

        for song in songs:
            rank = song.select_one('span.rank').text.strip()
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            song_list.append((rank, title, artist))

        random_song = random.choice(song_list)
        time.sleep(1)
        print(f"[이 노래가 좋을 거 같아요!]")
        time.sleep(1)
        print(f'\n[추천 곡: {random_song[1]} | 아티스트: {random_song[2]}]')
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')