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
