import threading
# Test threading daemon status
def test_daemon():
    print('Start')
    time.sleep(2)
    print('Exit')

t = threading.Thread(target=test_daemon, daemon=True)
t.start()
print('Main thread')

# Test threading join()
def test_join():
    print('Start')
    time.sleep(2)
    print('Exit')

t = threading.Thread(target=test_join)
t.start()
t.join()
print('Main thread')

# Test threading with lock
def test_lock(lock):
    lock.acquire()
    print('Start')
    time.sleep(2)
    print('Exit')
    lock.release()

lock = threading.Lock()
t = threading.Thread(target=test_lock, args=(lock,))
t.start()
t.join()
print('Main thread')

# Test threading with rlock
def test_rlock(lock):
    lock.acquire()
    print('Start')
    time.sleep(2)
