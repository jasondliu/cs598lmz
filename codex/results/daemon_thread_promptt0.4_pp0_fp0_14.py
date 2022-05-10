import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print('Starting:')
        time.sleep(5)
        print('Exiting')

    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)

    def non_daemon():
        print('Starting')
        print('Exiting')

    t = threading.Thread(name='non-daemon', target=non_daemon)

    d.start()
    t.start()
    d.join()
    t.join()

# Test threading lock
def test_threading_lock():
    x = 0
    lock = threading.Lock()
    def increment_global():
        global x
        x += 1

    def task_of_thread(lock):
        for _ in range(100000):
            lock.acquire()
            increment_global()
            lock.release()

    def main():
        t1 = threading.Thread(target=task_of_thread, args=(lock,))
        t2 = threading.
