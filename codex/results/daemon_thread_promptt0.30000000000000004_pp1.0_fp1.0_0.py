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

    d.join()
    t.join()

# Test threading lock

def test_threading_lock():
    x = 0

    def increment_global():
        global x
        x += 1

    def taskofThread(lock):
        for _ in range(100000):
            lock.acquire()
            increment_global()
            lock.release()

    def main_task
