import threading
# Test threading daemon

def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=test_daemon)
    d.setDaemon(True)
    d.start()
    d.join(1)
    print('main thread')

# Test threading lock

def test_lock():
    print('start')
    time.sleep(2)
    print('end')

if __name__ == '__main__':
    lock = threading.Lock()
    with lock:
        print('Lock is held')
        test_lock()

# Test threading RLock

def test_rlock():
    print('start')
    time.sleep(2)
    print('end')

if __name__ == '__main__':
    rlock = threading.RLock()
    with rlock:
        print('RLock is held')
        test_rlock()

# Test threading Semaphore
