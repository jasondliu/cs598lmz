import threading
# Test threading daemon

def test_daemon():
    print('start')
    time.sleep(1)
    print('end')

t = threading.Thread(target=test_daemon)
t.setDaemon(True)
t.start()

print('main thread')

# Test threading join

def test_join():
    print('start')
    time.sleep(1)
    print('end')

t = threading.Thread(target=test_join)
t.start()
t.join()

print('main thread')

# Test threading lock

lock = threading.Lock()

def test_lock():
    with lock:
        print('start')
        time.sleep(1)
        print('end')

t1 = threading.Thread(target=test_lock)
t2 = threading.Thread(target=test_lock)
t1.start()
t2.start()

print('main thread')

# Test threading RLock

rlock = threading.RLock()

def test_rlock():
