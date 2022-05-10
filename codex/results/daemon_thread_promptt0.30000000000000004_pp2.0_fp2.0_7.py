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
def test_lock(lock):
    with lock:
        print('Lock is held')

lock = threading.Lock()

w = threading.Thread(target=test_lock, args=(lock,))
nw = threading.Thread(target=test_lock, args=(lock,))

w.start()
nw.start()

w.join()
nw.join()

# Test threading rlock
def test_rlock(rlock):
    with rlock:
        print('rlock is held')

r
