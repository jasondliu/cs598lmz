import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print('Starting:', threading.current_thread().name)
        time.sleep(2)
        print('Exiting :', threading.current_thread().name)
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    d.start()
    d.join()
    print('Exiting main thread')

# Test threading lock
def test_threading_lock():
    lock = threading.Lock()
    def worker_with(lock):
        with lock:
            print(threading.current_thread().name, 'start')
            time.sleep(2)
            print(threading.current_thread().name, 'end')
    def worker_no_with(lock):
        lock.acquire()
        try:
            print(threading.current_thread().name, 'start')
            time.sleep(2)
            print(threading.current_thread().name, 'end')
        finally:
            lock.release
