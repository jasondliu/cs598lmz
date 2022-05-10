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

def test_lock():
    with lock:
        print('Lock is held')

t = threading.Thread(target=test_lock)
t.start()
t.join()

# Test threading rlock
rlock = threading.RLock()

def test_rlock():
    with rlock:
        print('RLock is held')

t = threading.Thread(target=test_rlock)
t.start()
t.join()

# Test threading sem
