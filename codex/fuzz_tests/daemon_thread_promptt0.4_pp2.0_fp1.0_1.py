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

# Test threading lock
lock = threading.Lock()

def test_lock():
    print('thread start')
    lock.acquire()
    print('thread acquire')
    time.sleep(2)
    print('thread release')
    lock.release()

t = threading.Thread(name='lock', target=test_lock)
t.start()

# Test threading with
with lock:
    print('with start')
    time.sleep(2)
    print('with end')

# Test threading semaphore
semaphore = threading.Semaphore(3)

