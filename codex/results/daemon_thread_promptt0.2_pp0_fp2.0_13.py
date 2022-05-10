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

print('end')

# Test threading lock
lock = threading.Lock()

def test_lock():
    print('start')
    lock.acquire()
    print('acquired')
    time.sleep(2)
    print('stop')
    lock.release()

t1 = threading.Thread(name='t1', target=test_lock)
t2 = threading.Thread(name='t2', target=test_lock)

t1.start()
t2.start()

t1.join()
t2.join
