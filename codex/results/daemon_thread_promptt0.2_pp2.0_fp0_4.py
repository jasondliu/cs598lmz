import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

def non_daemon():
    print('start')
    print('end')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
lock = threading.Lock()

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T1_job():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('T1:', A)
    lock.release()

def T2_job():
    global A, lock
    lock.acquire()

