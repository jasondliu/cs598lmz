import threading
# Test threading daemon and non-daemon thread
def daemon():
    print('Starting daemon thread')
    time.sleep(3)
    print('Exiting daemon thread')
def non_daemon():
    print('Starting non-daemon thread')
    print('Exiting non-daemon thread')
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
t = threading.Thread(name='non_daemon', target=non_daemon)
d.start()
t.start()

# Test threading lock
def threading_lock():
    count = 0
    lock = threading.Lock()
    def increment():
        nonlocal count
        lock.acquire()
        try:
            count += 1
        finally:
            lock.release()
    threads = []
    for i in range(100):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('Count: {0}'.format(count
