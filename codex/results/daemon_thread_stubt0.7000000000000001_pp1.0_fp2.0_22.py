import sys, threading

def run():
    while True:
        pass

thread = threading.Thread(target=run)
thread.start()

while True:
    pass

# 현재 os는 메모리가 초기화되지 않은 동안은 쓰레드를 생성할 수 없기 때문에 더 이상
# 쓰레드를 생성할 수 없습니다.
