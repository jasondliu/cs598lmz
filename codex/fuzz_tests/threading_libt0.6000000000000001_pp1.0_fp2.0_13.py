import threading
threading.current_thread().name #현재 실행중인 쓰레드의 이름을 리턴



# 쓰레드 생성
# threading.Thread(target=실행할함수, args=(인수,), name=쓰레드이름)

# 쓰레드 실행
# 쓰레드.start()

# 쓰레드 종료
# 쓰레드.join()



def func():
    print('func 실행중')
    time.sleep(3)
    print('func 종료')

t = threading.Thread(target=func, name='mythread')
t.start()
t.join()

print('main
