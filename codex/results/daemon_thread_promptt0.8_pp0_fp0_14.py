import threading
# Test threading daemon
# wait_for_event_timeout 함수 정의
def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    while not e.isSet():
        print("wait_for_event_timeout starting")
        e.wait(t)
    print("wait_for_event_timeout ending")

# Event 클래스 인스턴스를 사용하여 쓰레드를 생성한다.
e = threading.Event()
t1 = threading.Thread(name='block',
                      target=wait_for_event_timeout,
                      args=(e,2))
t1.start()

t2 = threading.Thread(name='nonblock',
                      target=wait_for_event_timeout,
                      args=(e,1))
t2.start()

print("Waiting before calling Event.set()")
time.sleep(3
