import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

d.start()
d.join(1)
print('d.isAlive()', d.isAlive())

# Test threading lock
lock = threading.Lock()

def test_with_lock(lock):
    with lock:
        print('Lock acquired via with')

def test_no_lock():
    print('Lock not acquired')

l = threading.Thread(name='with_lock', target=test_with_lock, args=(lock,))
nl = threading.Thread(name='no_lock', target=test_no_lock)

l.start()
nl.start()

l.join()
nl.join()

# Test threading event
event = threading.Event()

def waiter(event, n):
    print('{} waiting for event'.format(n))
    event
