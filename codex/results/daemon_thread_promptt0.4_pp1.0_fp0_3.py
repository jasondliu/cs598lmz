import threading
# Test threading daemon
def daemon():
    print('Start')
    time.sleep(2)
    print('End')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start')
    print('End')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
lock = threading.Lock()

def thread_1():
    lock.acquire()
    try:
        print('Thread-1')
    finally:
        lock.release()

def thread_2():
    lock.acquire()
    try:
        print('Thread-2')
    finally:
        lock.release()

t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)
t1.start()
t2.start()
t1.join()
t2
