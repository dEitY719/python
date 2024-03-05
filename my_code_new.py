# my_code.py는 py_lab.py에서 사용할 함수들을 모아둔 파일임
# 이 파일의 함수들을 동작 검증하기 위하여 실행 코드가 추가되어 있음
# 단, py_lab.py에서는 이 함수들만 공유하여 사용하는 것이 필요함

if  __name__ == '__main__' :
    print('my_code.py')

def add2(a, b):
    return a + b

def sub2(a, b):
    return a - b

if  __name__ == '__main__' :
    print(add2(1,2))
    print(sub2(1,2))
