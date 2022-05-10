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

def do_with_lock(lock):
    with lock:
        print('Lock is held')

lock.acquire()
print('Lock is held')
do_with_lock(lock)
lock.release()
print('Lock is released')

# Test threading RLock
lock = threading.RLock()

def do_with_lock(lock):
    with lock:
        print('Lock is held')

lock.acquire()
print('Lock is held')
do_with_
