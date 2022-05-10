import sys, threading

def run():
    while True:
        print("threading")
        time.sleep(1)

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

while True:
    print("main")
    time.sleep(1)

# 프로그램 종료시 스레드도 함께 종료됨
