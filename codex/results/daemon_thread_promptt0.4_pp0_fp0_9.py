import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(1)
    print('End daemon')
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start non-daemon')
    print('End non-daemon')
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
# Test threading lock
lock = threading.Lock()
def thread_1():
    print('Thread 1 start')
    lock.acquire()
    try:
        print('Thread 1 acquire lock')
    finally:
        lock.release()

def thread_2():
    print('Thread 2 start')
    lock.acquire()
    try:
        print('Thread 2 acquire lock')
    finally:
        lock.release()

t1 = threading.Thread(target=thread_1)
t1.start()
t2 = threading.Thread(target=thread_2)
t
