import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print('Starting:')
        time.sleep(2)
        print('Exiting')

    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)

    def non_daemon():
        print('Starting:')
        print('Exiting')

    t = threading.Thread(name='non-daemon', target=non_daemon)

    d.start()
    t.start()

# Test threading lock
def test_threading_lock():
    count = 0
    lock = threading.Lock()

    def increment():
        global count
        lock.acquire()
        count += 1
        lock.release()

    def run_threads(n):
        threads = []
        for i in range(n):
            t = threading.Thread(target=increment)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    run_threads(10)
   
