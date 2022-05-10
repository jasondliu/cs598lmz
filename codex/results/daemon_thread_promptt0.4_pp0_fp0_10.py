import threading
# Test threading daemon
def daemon():
    print('Start')
    time.sleep(5)
    print('Exit')

def non_daemon():
    print('Start')
    print('Exit')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
lock = threading.Lock()
def run(n):
    lock.acquire()
    print('thread %s is running' % n)
    lock.release()

def run_with_lock(n):
    lock.acquire()
    try:
        print('thread %s is running' % n)
    finally:
        lock.release()

def run_with_rlock(n):
    lock.acquire()
    try:
        print('thread %s is running' % n)
    finally:
        lock.release()

