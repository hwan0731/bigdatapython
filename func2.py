import requests
from bs4 import BeautifulSoup
import random
import time

def m100(num_songs):
    """멜론 실시간 차트에서 지정된 개수의 곡 정보를 출력합니다."""
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTPError 발생 시 예외를 발생시킵니다.
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')

        print(f"\n{'='*30}")
        print(f"멜론 실시간 차트 Top {num_songs}")
        print(f"{'='*30}")

        for index, song in enumerate(songs):
            if index >= num_songs:
                break

            rank = song.select_one('td:nth-child(2) > div.wrap > input[title="곡 순위"]').get('value').strip()
            title = song.select_one('div.ellipsis.rank01 > span > a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 > span').text.strip()

            print(f"{rank}. {title} - {artist}")
            time.sleep(0.1) # 과도한 요청 방지

    except requests.exceptions.RequestException as e:
        print(f"요청 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")

def recommend_song():
    """간단한 AI 추천 (랜덤) 기능을 수행합니다."""
    songs = [
        "아이브 - LOVE DIVE",
        "뉴진스 - Hype Boy",
        "르세라핌 - FEARLESS",
        "세븐틴 - Super",
        "BTS - Dynamite",
        "블랙핑크 - Pink Venom",
        "임영웅 - 사랑은 늘 도망가",
        "아이유 - Strawberry Moon",
        "데이식스 - 예뻤어",
        "잔나비 - 주저하는 연인들을 위해"
    ]
    recommended = random.choice(songs)
    print(f"\nAI 추천곡: {recommended}")

def search_artist():
    """가수 이름을 검색하는 기능을 수행합니다 (현재는 간단한 예시)."""
    artist_name = input("검색할 가수 이름을 입력하세요: ")
    print(f"\n'{artist_name}' 검색 결과 (간단한 예시):")
    # 실제 웹 검색 또는 데이터베이스 연동 로직이 필요합니다.
    if artist_name == "아이유":
        print("- 아이유의 주요 곡: Blueming, 밤편지, Celebrity")
    elif artist_name == "BTS":
        print("- BTS의 주요 곡: Butter, DNA, Spring Day")
    else:
        print("- 검색 결과가 없습니다.")

print("=================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("=================")

n_str = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n_str} ")

if n_str == '1':
    m100(100)
elif n_str == '2':
    m100(50)
elif n_str == '3':
    m100(10)
elif n_str == '4':
    recommend_song()
elif n_str == '5':
    search_artist()
else:
    print("잘못된 메뉴 선택입니다.")

    import requests
from bs4 import BeautifulSoup
import random
import time

def m100(num_songs):
    """멜론 실시간 차트에서 지정된 개수의 곡 정보를 출력합니다."""
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')

        print(f"\n{'='*30}")
        print(f"멜론 실시간 차트 Top {num_songs}")
        print(f"{'='*30}")

        for index, song in enumerate(songs):
            if index >= num_songs:
                break

            rank_element = song.select_one('td:nth-child(2) > div.wrap > input[title="곡 순위"]')
            title_element = song.select_one('div.ellipsis.rank01 > span > a')
            artist_element = song.select_one('div.ellipsis.rank02 > span')

            if rank_element:
                rank = rank_element.get('value').strip()
            else:
                rank = "순위 정보 없음"

            if title_element:
                title = title_element.text.strip()
            else:
                title = "제목 정보 없음"

            if artist_element:
                artist = artist_element.text.strip()
            else:
                artist = "아티스트 정보 없음"

            print(f"{rank}. {title} - {artist}")
            time.sleep(0.1)

    except requests.exceptions.RequestException as e:
        print(f"요청 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")

def recommend_song():
    """간단한 AI 추천 (랜덤) 기능을 수행합니다."""
    songs = [
        "아이브 - LOVE DIVE",
        "뉴진스 - Hype Boy",
        "르세라핌 - FEARLESS",
        "세븐틴 - Super",
        "BTS - Dynamite",
        "블랙핑크 - Pink Venom",
        "임영웅 - 사랑은 늘 도망가",
        "아이유 - Strawberry Moon",
        "데이식스 - 예뻤어",
        "잔나비 - 주저하는 연인들을 위해"
    ]
    recommended = random.choice(songs)
    print(f"\nAI 추천곡: {recommended}")

def search_artist():
    """가수 이름을 검색하는 기능을 수행합니다 (현재는 간단한 예시)."""
    artist_name = input("검색할 가수 이름을 입력하세요: ")
    print(f"\n'{artist_name}' 검색 결과 (간단한 예시):")
    if artist_name == "아이유":
        print("- 아이유의 주요 곡: Blueming, 밤편지, Celebrity")
    elif artist_name == "BTS":
        print("- BTS의 주요 곡: Butter, DNA, Spring Day")
    else:
        print("- 검색 결과가 없습니다.")

print("=================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("=================")

n_str = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n_str} ")

if n_str == '1':
    m100(100)
elif n_str == '2':
    m100(50)
elif n_str == '3':
    m100(10)
elif n_str == '4':
    recommend_song()
elif n_str == '5':
    search_artist()
else:
    print("잘못된 메뉴 선택입니다.")

    import requests
from bs4 import BeautifulSoup
import random
import time

def m100(num_songs):
    """멜론 실시간 차트에서 지정된 개수의 곡 정보를 출력합니다."""
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')

        print(f"\n{'='*30}")
        print(f"멜론 실시간 차트 Top {num_songs}")
        print(f"{'='*30}")

        for index, song in enumerate(songs):
            if index >= num_songs:
                break

            rank_element = song.select_one('td:nth-child(2) > div.wrap > input[title="곡 순위"]')
            title_element = song.select_one('div.ellipsis.rank01 > span > a')
            artist_element = song.select_one('div.ellipsis.rank02 > span')

            rank = rank_element.get('value').strip() if rank_element else "순위 정보 없음"
            title = title_element.text.strip() if title_element else "제목 정보 없음"
            artist = artist_element.text.strip() if artist_element else "아티스트 정보 없음"

            print(f"{rank}. {title} - {artist}")
            time.sleep(0.1)

    except requests.exceptions.RequestException as e:
        print(f"요청 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")

def recommend_song():
    """간단한 AI 추천 (랜덤) 기능을 수행합니다."""
    songs = [
        "아이브 - LOVE DIVE",
        "뉴진스 - Hype Boy",
        "르세라핌 - FEARLESS",
        "세븐틴 - Super",
        "BTS - Dynamite",
        "블랙핑크 - Pink Venom",
        "임영웅 - 사랑은 늘 도망가",
        "아이유 - Strawberry Moon",
        "데이식스 - 예뻤어",
        "잔나비 - 주저하는 연인들을 위해"
    ]
    recommended = random.choice(songs)
    print(f"\nAI 추천곡: {recommended}")

def search_artist():
    """가수 이름을 검색하는 기능을 수행합니다 (현재는 간단한 예시)."""
    artist_name = input("검색할 가수 이름을 입력하세요: ")
    print(f"\n'{artist_name}' 검색 결과 (간단한 예시):")
    if artist_name == "아이유":
        print("- 아이유의 주요 곡: Blueming, 밤편지, Celebrity")
    elif artist_name == "BTS":
        print("- BTS의 주요 곡: Butter, DNA, Spring Day")
    else:
        print("- 검색 결과가 없습니다.")

print("=================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("=================")

n_str = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n_str} ")

if n_str == '1':
    m100(100)
elif n_str == '2':
    m100(50)
elif n_str == '3':
    m100(10)
elif n_str == '4':
    recommend_song()
elif n_str == '5':
    search_artist()
else:
    print("잘못된 메뉴 선택입니다.")

    import requests
from bs4 import BeautifulSoup
import random
import time
import csv  # CSV 파일 처리를 위해 import

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


def m_save_csv(d):
    filename="melon_top100.csv"
    song_list = []
    print(d)
    time.sleep(1)
    print(f"[멜론 Top 100 차트 데이터를 '{filename}' 파일로 저장합니다.]")
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')

        for song in songs:
            rank = song.select_one('span.rank').text.strip()
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            # Store as tuple (rank, title, artist)
            song_list.append((rank, title, artist))
    else:
         print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')
         print("===================") # Add separator
         return # Exit the function if scraping failed


    if not song_list:
        print("[저장할 차트 데이터가 없습니다.]")
        print("===================") # Add separator
        return

    # 2. CSV 파일 쓰기
    try:
        # newline='' : CSV 파일에 빈 줄이 추가되는 것을 방지 (특히 Windows)
        # encoding='utf-8-sig' : Excel에서 한글이 깨지지 않도록 함 (BOM 포함 UTF-8)
        with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            # Use csv.writer for lists of tuples/lists
            writer = csv.writer(csvfile)

            # Write header row manually
            writer.writerow(['순위', '제목', '아티스트'])

            # Write data rows
            writer.writerows(song_list)

        print(f"[성공: '{filename}' 파일에 Top {len(song_list)} 차트를 저장했습니다.]")
    except IOError as e:
        print(f"[오류: 파일 쓰기 중 문제가 발생했습니다 - {e}]")
    except Exception as e:
        print(f"[오류: CSV 저장 중 예상치 못한 오류 발생 - {e}]")

    print("===================") # Add separator

    import requests
from bs4 import BeautifulSoup
import random
import time


print("==========================")
print("| 1. 멜론 차트 TOP 100곡  |")
print("| 2. 멜론 차트 TOP 50곡   |")
print("| 3. 멜론 차트 TOP 10곡   |")
print("| 4. 멜론 차트 AI 추천곡  |")
print("| 5. 가수 이름 검색       |")
print("| 6. 파일에 저장(멜론 100)|")
print("==========================")

a = "<멜론 차트 TOP 100곡>"
b = "<멜론 차트 TOP 50곡>"
c = "<멜론 차트 TOP 10곡>"
d = "<멜론 차트 AI 추천곡>"
e = "<가수 이름 검색>"

n = input("[원하시는 서비스에 해당하는 번호를 입력하세요.]: ")
if n == "1":
    print("멜론100을 출력하는 기능")

elif n == "2":
    print(b)
    time.sleep(1)
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
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. | 상태 코드: {response.status_code}]')

elif n == "3":
    print(c)
    time.sleep(1)
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
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')

elif n == "4":
    print(d)
    time.sleep(1)
    print("[좋아요! 제가 열심히 찾아서 사용자님께 노래를 한 곡 추천할게요.]")
    time.sleep(1)
    print(f"[두구두구둥...]")

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

elif n == "5":
    print(e)
    time.sleep(1)
    s = input("[검색하고 싶은 가수의 이름을 입력하세요.]: ")
    print(f"[<{s}>의 노래를 검색 중이에요...]")
    time.sleep(1)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')
        found_songs = []

        for song in songs:
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            if s.lower() in artist.lower():
                rank = song.select_one('span.rank').text.strip()
                title = song.select_one('div.ellipsis.rank01 a').text.strip()
                found_songs.append((rank, title, artist))

        if found_songs:
            print(f"[<{s}>의 노래 목록이에요.]")
            for song in found_songs:
                print(f'{song[0]}위 | 제목: {song[1]} | 아티스트: {song[2]}')
        else:
            print(f"[TOP 100곡 내 <{s}>의 노래가 없어요.]")
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')

else:
    print(f"[<{n}>번에 해당하는 서비스가 없어요. 1~5번 중에 선택해 주세요.]")


    import requests
from bs4 import BeautifulSoup
import random
import time
import csv  # CSV 파일 처리를 위해 import

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


def m_save_csv(d):
    filename="melon_top100.csv"
    song_list = []
    print(d)
    time.sleep(1)
    print(f"[멜론 Top 100 차트 데이터를 '{filename}' 파일로 저장합니다.]")
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')

        for song in songs:
            rank = song.select_one('span.rank').text.strip()
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            # Store as tuple (rank, title, artist)
            song_list.append((rank, title, artist))
    else:
         print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')
         print("===================") # Add separator
         return # Exit the function if scraping failed


    if not song_list:
        print("[저장할 차트 데이터가 없습니다.]")
        print("===================") # Add separator
        return

    # 2. CSV 파일 쓰기
    try:
        # newline='' : CSV 파일에 빈 줄이 추가되는 것을 방지 (특히 Windows)
        # encoding='utf-8-sig' : Excel에서 한글이 깨지지 않도록 함 (BOM 포함 UTF-8)
        with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            # Use csv.writer for lists of tuples/lists
            writer = csv.writer(csvfile)

            # Write header row manually
            writer.writerow(['순위', '제목', '아티스트'])

            # Write data rows
            writer.writerows(song_list)

        print(f"[성공: '{filename}' 파일에 Top {len(song_list)} 차트를 저장했습니다.]")
    except IOError as e:
        print(f"[오류: 파일 쓰기 중 문제가 발생했습니다 - {e}]")
    except Exception as e:
        print(f"[오류: CSV 저장 중 예상치 못한 오류 발생 - {e}]")

    print("===================") # Add separator