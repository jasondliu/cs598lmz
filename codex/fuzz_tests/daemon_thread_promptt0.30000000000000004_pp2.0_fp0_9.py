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
lock = threading.Lock()

def test_lock(i):
    lock.acquire()
    try:
        print('hello world', i)
    finally:
        lock.release()

for num in range(10):
    t = threading.Thread(target=test_lock, args=(num,))
    t.start()

# Test threading local
local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s
