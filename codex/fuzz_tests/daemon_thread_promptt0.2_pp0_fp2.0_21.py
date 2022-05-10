import threading
# Test threading daemon
def test_thread_daemon():
    def daemon():
        print('Starting:')
        time.sleep(2)
        print('Exiting')
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    d.start()
    d.join()
    print('d.isAlive()', d.isAlive())

# Test threading lock
def test_thread_lock():
    lock = threading.Lock()
    def worker_with(lock):
        with lock:
            print(threading.current_thread().getName(), 'start')
            time.sleep(2)
            print(threading.current_thread().getName(), 'end')
    def worker_no_with(lock):
        lock.acquire()
        try:
            print(threading.current_thread().getName(), 'start')
            time.sleep(2)
            print(threading.current_thread().getName(), 'end')
        finally:
            lock.release()
    t1 = threading.
