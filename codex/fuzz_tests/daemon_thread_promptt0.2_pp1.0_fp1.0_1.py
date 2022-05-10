import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

d.start()
d.join()

print('main thread')

# Test threading lock
lock = threading.Lock()

def test_lock(n):
    lock.acquire()
    try:
        print('Thread %s\n' % n)
    finally:
        lock.release()

def test_lock_with(n):
    with lock:
        print('Thread %s\n' % n)

t1 = threading.Thread(target=test_lock, args=(1,))
t2 = threading.Thread(target=test_lock, args=(2,))
t3 = threading.Thread(target=test_lock_with, args=(3,))
t4 = threading.Thread(target=test_lock_with, args=(4,))

t1.start()
t
