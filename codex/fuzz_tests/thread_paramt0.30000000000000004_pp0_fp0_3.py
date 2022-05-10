import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

# 간단한 정렬 기능
# sorted(iterable, key=None, reverse=False)
# key : 각 항목을 정렬할 때 키 함수를 사용하여 각 항목의 키를 생성
# reverse : 역순으로 정렬할지 여부

# 문자열 내림차순으로 정렬
sorted('Hello, world!', reverse=True)

# 문자열 내림차순으로 정렬
sorted('Hello, world!', key
