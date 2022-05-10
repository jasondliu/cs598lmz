import threading
# Test threading daemon
def daemon():
    print('Start')
    time.sleep(5)
    print('End')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start')
    print('End')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading lock
lock = threading.Lock()

def thread_1():
    print('Thread 1 start')
    lock.acquire()
    print('Thread 1 acquire lock')
    time.sleep(3)
    print('Thread 1 release lock')
    lock.release()
    print('Thread 1 end')

def thread_2():
    print('Thread 2 start')
    lock.acquire()
    print('Thread 2 acquire lock')
    time.sleep(2)
    print('Thread 2 release lock')
    lock.release()
    print('Thread 2 end')

t1 = threading.Thread(name
