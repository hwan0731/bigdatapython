import csv

def read_csv(filename):
    """CSV 파일을 읽어 내용을 출력합니다."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"오류: '{filename}' 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류: {e}")

# 예시: 'example.csv' 파일 읽기
read_csv('example.csv')

import csv

def write_csv(filename, data):
    """데이터를 CSV 파일에 씁니다."""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"'{filename}' 파일에 데이터가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"오류: {e}")

# 예시: 데이터를 'output.csv' 파일에 쓰기
data = [['Name', 'Age', 'City'], ['Alice', '25', 'Seoul'], ['Bob', '30', 'Busan']]
write_csv('output.csv', data)

import csv

def read_csv(filename):
    """CSV 파일을 읽어 내용을 출력합니다."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"오류: '{filename}' 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류: {e}")

def write_csv(filename, data):
    """데이터를 CSV 파일에 씁니다."""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"'{filename}' 파일에 데이터가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"오류: {e}")

# 예시: 'example.csv' 파일 읽기
read_csv('example.csv')

# 예시: 데이터를 'output.csv' 파일에 쓰기
data = [['Name', 'Age', 'City'], ['Alice', '25', 'Seoul'], ['Bob', '30', 'Busan']]
write_csv('output.csv', data)

import csv

# 원본 CSV 파일 읽기 및 데이터 변환 후 새 파일에 쓰기
with open('input.csv', 'r', encoding='utf-8') as infile:
    with open('output.csv', 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            # 데이터 변환 예시 (모든 문자열을 대문자로 변환)
            transformed_row = [item.upper() if isinstance(item, str) else item for item in row]
            writer.writerow(transformed_row)

import csv
import os

# 쓸 데이터 준비
data = [
    ['이름', '나이', '직업'],
    ['홍길동', '30', '개발자'],
    ['김철수', '25', '디자이너'],
    ['이영희', '35', '매니저']
]

# 폴더 존재 확인 및 생성
output_path = 'output.csv'
output_dir = os.path.dirname(output_path)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

try:
    with open(output_path, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
    print(f"'{output_path}' 파일에 데이터를 성공적으로 썼습니다.")
except PermissionError:
    print(f"'{output_path}' 파일에 접근 권한이 없습니다.")
except Exception as e:
    print(f"파일 쓰기 오류: {e}")

import csv
import os

def process_csv(input_path, output_path):
    """
    CSV 파일을 읽고, 처리한 후 결과를 새 CSV 파일에 쓰는 함수
    
    Args:
        input_path (str): 입력 CSV 파일 경로
        output_path (str): 출력 CSV 파일 경로
    
    Returns:
        bool: 처리 성공 여부
    """
    # 입력 파일 존재 여부 확인
    if not os.path.exists(input_path):
        print(f"'{input_path}' 파일이 존재하지 않습니다.")
        return False
    
    # 출력 디렉토리 존재 여부 확인 및 생성
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 인코딩 목록
    encodings = ['utf-8', 'cp949', 'euc-kr']
    
    # 데이터를 저장할 리스트
    data = []
    
    # 파일 읽기 시도
    success = False
    for encoding in encodings:
        try:
            with open(input_path, 'r', encoding=encoding) as infile:
                csv_reader = csv.reader(infile)
                data = list(csv_reader)
            success = True
            print(f"'{input_path}' 파일을 {encoding} 인코딩으로 성공적으로 읽었습니다.")
            break
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"파일 읽기 오류: {e}")
            return False
    
    if not success:
        print(f"'{input_path}' 파일을 읽을 수 없습니다. 지원되는 인코딩 형식이 아닙니다.")
        return False
    
    # 데이터 처리 (예: 모든 문자열을 대문자로 변환)
    processed_data = []
    for row in data:
        processed_row = []
        for item in row:
            if isinstance(item, str):
                processed_row.append(item.upper())
            else:
                processed_row.append(item)
        processed_data.append(processed_row)
    
    # 처리된 데이터 쓰기
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            csv_writer.writerows(processed_data)
        print(f"'{output_path}' 파일에 처리된 데이터를 성공적으로 썼습니다.")
        return True
    except PermissionError:
        print(f"'{output_path}' 파일에 접근 권한이 없습니다.")
        return False
    except Exception as e:
        print(f"파일 쓰기 오류: {e}")
        return False

# 실행 예
if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output.csv"
    
    # 테스트용 입력 파일 생성
    if not os.path.exists(input_file):
        try:
            with open(input_file, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerows([
                    ['이름', '나이', '직업'],
                    ['홍길동', '30', '개발자'],
                    ['김철수', '25', '디자이너'],
                    ['이영희', '35', '매니저']
                ])
            print(f"테스트용 '{input_file}' 파일을 생성했습니다.")
        except Exception as e:
            print(f"테스트 파일 생성 오류: {e}")
    
    # CSV 처리 함수 호출
    process_csv(input_file, output_file)

import pandas as pd
import os

def safe_read_csv(file_path):
    """
    안전하게 CSV 파일을 읽는 함수
    
    Args:
        file_path (str): 읽을 CSV 파일 경로
    
    Returns:
        DataFrame 또는 None: 성공 시 데이터프레임, 실패 시 None
    """
    if not os.path.exists(file_path):
        print(f"'{file_path}' 파일이 존재하지 않습니다.")
        return None
    
    # 인코딩 목록
    encodings = ['utf-8', 'cp949', 'euc-kr']
    
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            print(f"'{file_path}' 파일을 {encoding} 인코딩으로 성공적으로 읽었습니다.")
            return df
        except UnicodeDecodeError:
            continue
        except pd.errors.EmptyDataError:
            print(f"'{file_path}' 파일이 비어 있습니다.")
            return pd.DataFrame()
        except pd.errors.ParserError:
            print(f"'{file_path}' 파일의 형식이 올바르지 않습니다.")
            return None
        except Exception as e:
            print(f"파일 읽기 오류: {e}")
            return None
    
    print(f"'{file_path}' 파일을 읽을 수 없습니다. 지원되는 인코딩 형식이 아닙니다.")
    return None

def safe_write_csv(df, file_path):
    """
    안전하게 CSV 파일을 쓰는 함수
    
    Args:
        df (DataFrame): 쓸 데이터프레임
        file_path (str): 쓸 CSV 파일 경로
    
    Returns:
        bool: 성공 여부
    """
    # 출력 디렉토리 존재 여부 확인 및 생성
    output_dir = os.path.dirname(file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"'{file_path}' 파일에 데이터를 성공적으로 썼습니다.")
        return True
    except PermissionError:
        print(f"'{file_path}' 파일에 접근 권한이 없습니다.")
        return False
    except Exception as e:
        print(f"파일 쓰기 오류: {e}")
        return False

# 실행 예제
if __name__ == "__main__":
    # 테스트용 입력 파일 생성
    input_file = "input_pandas.csv"
    output_file = "output_pandas.csv"
    
    # 테스트 데이터
    test_data = {
        '이름': ['홍길동', '김철수', '이영희'],
        '나이': [30, 25, 35],
        '직업': ['개발자', '디자이너', '매니저']
    }
    test_df = pd.DataFrame(test_data)
    
    # 테스트 파일 생성
    if not os.path.exists(input_file):
        try:
            test_df.to_csv(input_file, index=False, encoding='utf-8')
            print(f"테스트용 '{input_file}' 파일을 생성했습니다.")
        except Exception as e:
            print(f"테스트 파일 생성 오류: {e}")
    
    # CSV 파일 읽기
    df = safe_read_csv(input_file)
    
    if df is not None:
        # 데이터 처리 (예: 나이에 5 더하기)
        if '나이' in df.columns:
            df['나이'] = df['나이'] + 5
        
        # 처리된 데이터 쓰기
        safe_write_csv(df, output_file)

import csv
import os

# 예제 1: CSV 파일 쓰기
def write_csv_example():
    try:
        # 데이터 생성
        data = [
            ['이름', '나이', '직업'],
            ['홍길동', '30', '개발자'],
            ['김철수', '25', '디자이너'],
            ['이영희', '35', '매니저']
        ]
        
        # CSV 파일 쓰기
        with open('output.csv', 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        print("'output.csv' 파일에 데이터가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"CSV 쓰기 오류: {e}")

# 예제 2: CSV 파일 읽기
def read_csv_example(file_path):
    # 파일 존재 여부 확인
    if not os.path.exists(file_path):
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다.")
        return
    
    try:
        # CSV 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    except UnicodeDecodeError:
        try:
            # UTF-8 실패 시 CP949로 시도
            with open(file_path, 'r', encoding='cp949') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    print(row)
        except Exception as e:
            print(f"CSV 읽기 오류: {e}")
    except Exception as e:
        print(f"CSV 읽기 오류: {e}")

# 예제 3: CSV 파일 처리 (읽기 → 처리 → 쓰기)
def process_csv_example(input_path, output_path):
    # 입력 파일 존재 여부 확인
    if not os.path.exists(input_path):
        print(f"오류: '{input_path}' 파일을 찾을 수 없습니다.")
        
        # 입력 파일이 없는 경우 새로 생성 (테스트 목적)
        try:
            with open(input_path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerows([
                    ['이름', '나이', '직업'],
                    ['홍길동', '30', '개발자'],
                    ['김철수', '25', '디자이너'],
                    ['이영희', '35', '매니저']
                ])
            print(f"'{input_path}' 파일을 새로 생성했습니다.")
        except Exception as e:
            print(f"파일 생성 오류: {e}")
            return
    
    try:
        # 데이터 읽기
        rows = []
        with open(input_path, 'r', encoding='utf-8') as infile:
            csv_reader = csv.reader(infile)
            rows = list(csv_reader)
        
        # 데이터 처리 (예: 모든 문자열을 대문자로 변환)
        processed_rows = []
        for row in rows:
            processed_row = [item.upper() if isinstance(item, str) else item for item in row]
            processed_rows.append(processed_row)
        
        # 처리된 데이터 쓰기
        with open(output_path, 'w', encoding='utf-8', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            csv_writer.writerows(processed_rows)
        
        print(f"'{output_path}' 파일에 처리된 데이터가 성공적으로 저장되었습니다.")
    except UnicodeDecodeError:
        # UTF-8 실패 시 CP949로 시도
        try:
            with open(input_path, 'r', encoding='cp949') as infile:
                csv_reader = csv.reader(infile)
                rows = list(csv_reader)
            
            # 데이터 처리 (예: 모든 문자열을 대문자로 변환)
            processed_rows = []
            for row in rows:
                processed_row = [item.upper() if isinstance(item, str) else item for item in row]
                processed_rows.append(processed_row)
            
            # 처리된 데이터 쓰기
            with open(output_path, 'w', encoding='utf-8', newline='') as outfile:
                csv_writer = csv.writer(outfile)
                csv_writer.writerows(processed_rows)
            
            print(f"'{output_path}' 파일에 처리된 데이터가 성공적으로 저장되었습니다.")
        except Exception as e:
            print(f"CSV 처리 오류: {e}")
    except Exception as e:
        print(f"CSV 처리 오류: {e}")

# 메인 함수
if __name__ == "__main__":
    # 예제 1: CSV 파일 읽기
    read_csv_example('example.csv')
    
    # 예제 2: CSV 파일 쓰기
    write_csv_example()
    
    # 예제 3: CSV 파일 처리
    process_csv_example('input.csv', 'processed_output.csv')
    
    print("모든 작업이 완료되었습니다.")

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
    print("6. 파일에 저장(멜론100)")
    print("=================")

  
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
        
        import csv
import os

# CSV 파일 쓰기 함수
def write_csv_file():
    try:
        # 데이터 준비
        data = [
            ['이름', '나이', '직업'],
            ['홍길동', '30', '개발자'],
            ['김철수', '25', '디자이너'],
            ['이영희', '35', '매니저']
        ]
        
        # CSV 파일 쓰기
        with open('output.csv', 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        print("'output.csv' 파일에 데이터가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"파일 쓰기 오류: {e}")

# CSV 파일 읽기 함수
def read_csv_file(file_path):
    # 파일 존재 여부 확인
    if not os.path.exists(file_path):
        print(f"'{file_path}' 파일이 존재하지 않습니다.")
        return None
    
    # 다양한 인코딩으로 시도
    encodings = ['utf-8', 'cp949', 'euc-kr']
    
    for encoding in encodings:
        try:
            rows = []
            with open(file_path, 'r', encoding=encoding) as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)
            print(f"'{file_path}' 파일을 {encoding} 인코딩으로 성공적으로 읽었습니다.")
            return rows
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"파일 읽기 오류: {e}")
            return None
    
    print(f"'{file_path}' 파일을 읽을 수 없습니다. 지원되는 인코딩 형식이 아닙니다.")
    return None

# CSV 파일 처리 함수
def process_csv_file(input_path, output_path):
    # 입력 파일 존재 여부 확인
    if not os.path.exists(input_path):
        print(f"'{input_path}' 파일이 존재하지 않습니다. 새로운 파일을 생성합니다.")
        
        # 테스트용 입력 파일 생성
        create_test_csv(input_path)
        
    # 파일 읽기
    rows = read_csv_file(input_path)
    
    if rows is None or len(rows) == 0:
        print("처리할 데이터가 없습니다.")
        return
    
    # 데이터 처리 (예: 모든 문자열을 대문자로 변환)
    processed_rows = []
    for row in rows:
        processed_row = [str(item).upper() for item in row]
        processed_rows.append(processed_row)
    
    # 처리된 데이터 쓰기
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(processed_rows)
        print(f"'{output_path}' 파일에 처리된 데이터가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"파일 쓰기 오류: {e}")

# 테스트용 CSV 파일 생성 함수
def create_test_csv(file_path):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows([
                ['이름', '나이', '직업'],
                ['홍길동', '30', '개발자'],
                ['김철수', '25', '디자이너'],
                ['이영희', '35', '매니저']
            ])
        print(f"테스트용 '{file_path}' 파일을 생성했습니다.")
    except Exception as e:
        print(f"파일 생성 오류: {e}")

# 메인 함수
def main():
    # 파일 경로 설정
    input_file = 'input.csv'
    output_file = 'processed_output.csv'
    
    # CSV 파일 쓰기 예제
    write_csv_file()
    
    # CSV 파일 처리 예제
    process_csv_file(input_file, output_file)
    
    print("모든 CSV 처리 작업이 완료되었습니다.")

# 프로그램 실행
if __name__ == "__main__":
    main()

import csv
import os

# CSV 파일 쓰기 함수
def write_csv_file():
    # 데이터 준비
    data = [
        ['이름', '나이', '직업'],
        ['홍길동', '30', '개발자'],
        ['김철수', '25', '디자이너'],
        ['이영희', '35', '매니저']
    ]
    
    try:
        # CSV 파일 쓰기
        with open('output.csv', 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        print("'output.csv' 파일에 데이터가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"파일 쓰기 오류: {e}")

# 테스트용 CSV 파일 생성 함수
def create_test_csv(file_path):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows([
                ['이름', '나이', '직업'],
                ['홍길동', '30', '개발자'],
                ['김철수', '25', '디자이너'],
                ['이영희', '35', '매니저']
            ])
        print(f"테스트용 '{file_path}' 파일을 생성했습니다.")
    except Exception as e:
        print(f"파일 생성 오류: {e}")

# CSV 파일 읽기 함수
def read_csv_file(file_path):
    # 파일 존재 여부 확인
    if not os.path.exists(file_path):
        print(f"'{file_path}' 파일이 존재하지 않습니다.")
        return None
    
    # 다양한 인코딩으로 시도
    encodings = ['utf-8', 'cp949', 'euc-kr']
    
    for encoding in encodings:
        try:
            rows = []
            with open(file_path, 'r', encoding=encoding) as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)
            print(f"'{file_path}' 파일을 {encoding} 인코딩으로 성공적으로 읽었습니다.")
            return rows
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"파일 읽기 오류: {e}")
            return None
    
    print(f"'{file_path}' 파일을 읽을 수 없습니다.")
    return None

# CSV 파일 처리 함수
def process_csv_file(input_path, output_path):
    # 입력 파일 존재 여부 확인
    if not os.path.exists(input_path):
        print(f"'{input_path}' 파일이 존재하지 않습니다. 새로운 파일을 생성합니다.")
        # 테스트용 입력 파일 생성
        create_test_csv(input_path)
    
    # 파일 읽기
    rows = read_csv_file(input_path)
    
    if rows is None or len(rows) == 0:
        print("처리할 데이터가 없습니다.")
        return
    
    # 데이터 처리 (예: 모든 문자열을 대문자로 변환)
    processed_rows = []
    for row in rows:
        processed_row = [str(item).upper() for item in row]
        processed_rows.append(processed_row)
    
    # 처리된 데이터 쓰기
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(processed_rows)
        print(f"'{output_path}' 파일에 처리된 데이터가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"파일 쓰기 오류: {e}")

# 메인 함수
if __name__ == "__main__":
    # 파일 경로 설정
    input_file = 'input.csv'
    output_file = 'processed_output.csv'
    
    # CSV 파일 쓰기 예제
    write_csv_file()
    
    # CSV 파일 처리 예제
    process_csv_file(input_file, output_file)
    
    print("모든 CSV 처리 작업이 완료되었습니다.")

import csv
import os

# CSV 파일 쓰기 함수
def write_csv_file():
    # 데이터 준비
    data = [
        ['이름', '나이', '직업'],
        ['홍길동', '30', '개발자'],
        ['김철수', '25', '디자이너'],
        ['이영희', '35', '매니저']
    ]
    
    try:
        # CSV 파일 쓰기
        with open('output.csv', 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        print("'output.csv' 파일에 데이터가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"파일 쓰기 오류: {e}")

# 테스트용 CSV 파일 생성 함수
def create_test_csv(file_path):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows([
                ['이름', '나이', '직업'],
                ['홍길동', '30', '개발자'],
                ['김철수', '25', '디자이너'],
                ['이영희', '35', '매니저']
            ])
        print(f"테스트용 '{file_path}' 파일을 생성했습니다.")
    except Exception as e:
        print(f"파일 생성 오류: {e}")

# CSV 파일 읽기 함수
def read_csv_file(file_path):
    # 파일 존재 여부 확인
    if not os.path.exists(file_path):
        print(f"'{file_path}' 파일이 존재하지 않습니다.")
        return None
    
    # 다양한 인코딩으로 시도
    encodings = ['utf-8', 'cp949', 'euc-kr']
    
    for encoding in encodings:
        try:
            rows = []
            with open(file_path, 'r', encoding=encoding) as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)
            print(f"'{file_path}' 파일을 {encoding} 인코딩으로 성공적으로 읽었습니다.")
            return rows
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"파일 읽기 오류: {e}")
            return None
    
    print(f"'{file_path}' 파일을 읽을 수 없습니다.")
    return None

# CSV 파일 처리 함수
def process_csv_file(input_path, output_path):
    # 입력 파일 존재 여부 확인
    if not os.path.exists(input_path):
        print(f"'{input_path}' 파일이 존재하지 않습니다. 새로운 파일을 생성합니다.")
        # 테스트용 입력 파일 생성
        create_test_csv(input_path)
    
    # 파일 읽기
    rows = read_csv_file(input_path)
    
    if rows is None or len(rows) == 0:
        print("처리할 데이터가 없습니다.")
        return
    
    # 데이터 처리 (예: 모든 문자열을 대문자로 변환)
    processed_rows = []
    for row in rows:
        processed_row = [str(item).upper() for item in row]
        processed_rows.append(processed_row)
    
    # 처리된 데이터 쓰기
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(processed_rows)
        print(f"'{output_path}' 파일에 처리된 데이터가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"파일 쓰기 오류: {e}")

# 메인 함수
if __name__ == "__main__":
    # 파일 경로 설정
    input_file = 'input.csv'
    output_file = 'processed_output.csv'
    
    # CSV 파일 쓰기 예제
    write_csv_file()
    
    # CSV 파일 처리 예제
    process_csv_file(input_file, output_file)
    
    print("모든 CSV 처리 작업이 완료되었습니다.")

    import requests
 from bs4 import BeautifulSoup
 import random
 import time
 
 url = 'https://www.melon.com/chart/index.htm'
 
 headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
 }
 
 response = requests.get(url, headers=headers)
 
 
 print("==========================")
 print("| 1. 멜론 차트 TOP 100곡 |")
 print("| 2. 멜론 차트 TOP 50곡  |")
 print("| 3. 멜론 차트 TOP 10곡  |")
 print("| 4. 멜론 차트 AI 추천곡 |")
 print("| 5. 가수 이름 검색      |")
 print("==========================")
 
 a = "<멜론 차트 TOP 100곡>"
 b = "<멜론 차트 TOP 50곡>"
 c = "<멜론 차트 TOP 10곡>"
 d = "<멜론 차트 AI 추천곡>"
 e = "<가수 이름 검색>"
 
 n = input("[원하시는 서비스에 해당하는 번호를 입력하세요.]: ")
 if n == "1":
     print(a)
     time.sleep(1)
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
     print("[죄송해요. 해당 서비스는 아직 준비 중이에요.]")
 else:
     print(f"[<{n}>번에 해당하는 서비스가 없어요. 1~5번 중에 선택해 주세요.]")

     import requests
from bs4 import BeautifulSoup
import random
import time

url = 'https://www.melon.com/chart/index.htm'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)


print("==========================")
print("| 1. 멜론 차트 TOP 100곡 |")
print("| 2. 멜론 차트 TOP 50곡  |")
print("| 3. 멜론 차트 TOP 10곡  |")
print("| 4. 멜론 차트 AI 추천곡 |")
print("| 5. 가수 이름 검색      |")
print("==========================")

a = "<멜론 차트 TOP 100곡>"
b = "<멜론 차트 TOP 50곡>"
c = "<멜론 차트 TOP 10곡>"
d = "<멜론 차트 AI 추천곡>"
e = "<가수 이름 검색>"

n = input("[원하시는 서비스에 해당하는 번호를 입력하세요.]: ")
if n == "1":
    print(a)
    time.sleep(1)
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


    import csv

data_to_write = [
    ['순위', '제목', '가수'],
    [1, '1노래', '1가수'],
    [2, '2노래', '2가수'],
    [3, '3노래', '3가수']
]
file_path = 'music.csv'
try:
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_to_write)

    print(f"'{file_path}' 파일이 성공적으로 생성되었습니다.")

except Exception as e:
    print(f"파일 쓰기 중 오류 발생: {e}")