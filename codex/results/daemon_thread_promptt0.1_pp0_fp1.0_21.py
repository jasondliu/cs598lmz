import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print('Starting:')
        time.sleep(2)
        print('Exiting')
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    d.start()
    d.join()

# Test threading lock
def test_threading_lock():
    lock = threading.Lock()
    def worker_with(lock):
        with lock:
            print(threading.current_thread().getName(), 'Started')
            time.sleep(0.2)
            print(threading.current_thread().getName(), 'Exiting')
    def worker_no_with(lock):
        lock.acquire()
        try:
            print(threading.current_thread().getName(), 'Started')
            time.sleep(0.2)
        finally:
            print(threading.current_thread().getName(), 'Exiting')
            lock.release()
    t1 = threading.Thread(target=worker_with
