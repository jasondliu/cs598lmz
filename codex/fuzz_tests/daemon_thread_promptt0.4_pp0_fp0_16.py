import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print 'Starting:', threading.currentThread().getName()
        time.sleep(2)
        print 'Exiting :', threading.currentThread().getName()

    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)

    def non_daemon():
        print 'Starting:', threading.currentThread().getName()
        print 'Exiting :', threading.currentThread().getName()

    t = threading.Thread(name='non-daemon', target=non_daemon)

    d.start()
    t.start()

# Test threading lock
def test_threading_lock():
    lock = threading.Lock()
    def worker_with(lock):
        with lock:
            print 'Lock acquired via with'

    def worker_no_with(lock):
        lock.acquire()
        try:
            print 'Lock acquired directly'
        finally:
            lock.release()

    w = threading.
