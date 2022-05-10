import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('stop')

d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

def non_daemon():
    print('start')
    print('stop')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
def test_lock():
    print('start')
    time.sleep(2)
    print('stop')

lock = threading.Lock()

def test_lock_with_lock():
    lock.acquire()
    test_lock()
    lock.release()

def test_lock_with_context_manager():
    with lock:
        test_lock()

t1 = threading.Thread(name='lock1', target=test_lock_with_lock)
t2 = threading.Thread(name='lock2
