import sys, threading

def run():
    while True:
        print('sub thread start')
        time.sleep(1)
        print('sub thread end')

t = threading.Thread(target=run)
t.setDaemon(True)

print('main thread start')
t.start()
time.sleep(0.5)
print('main thread end')

# main thread start
# sub thread start
# sub thread end
# main thread end

# 일반적으로 서버 프로그램을 만들 때 사용하는 방법
# 서버 코드 돌리고, Ctrl + c 로 종료할 수 있음
# setDaemon(True) 이렇게 설정하면, 메인 스레드
