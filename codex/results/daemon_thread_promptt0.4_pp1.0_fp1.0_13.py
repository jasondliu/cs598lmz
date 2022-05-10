import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print('Starting:', threading.currentThread().getName())
        time.sleep(2)
        print('Exiting :', threading.currentThread().getName())
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    d.start()
    d.join()

# Test threading lock
def test_threading_lock():
    def worker_with(lock):
        with lock:
            print(threading.currentThread().getName(), 'start')
            time.sleep(2)
            print(threading.currentThread().getName(), 'stop')
    def worker_no_with(lock):
        lock.acquire()
        try:
            print(threading.currentThread().getName(), 'start')
            time.sleep(2)
            print(threading.currentThread().getName(), 'stop')
        finally:
            lock.release()
    lock = threading.Lock()
    w = threading.Thread
