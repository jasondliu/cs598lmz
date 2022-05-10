import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print('Starting:')
        time.sleep(2)
        print('Exiting:')

    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)

    def non_daemon():
        print('Starting:')
        print('Exiting:')

    t = threading.Thread(name='non-daemon', target=non_daemon)

    d.start()
    t.start()
    d.join()
    t.join()

# Test threading lock
def test_threading_lock():
    lock = threading.Lock()
    def worker_with(lock):
        with lock:
            print(threading.current_thread().getName(), 'start')
            time.sleep(2)
            print(threading.current_thread().getName(), 'end')

    def worker_no_with(lock):
        lock.acquire()
        try:
            print(threading.current_thread().getName(), 'start
