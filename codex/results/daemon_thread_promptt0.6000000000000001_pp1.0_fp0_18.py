import threading
# Test threading daemon
def test_thread_daemon():
    def run():
        print('Thread is running')
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    t.join()
    print('Main thread is running')

# Test threading lock
lock = threading.Lock()
def test_thread_lock():
    def run():
        lock.acquire()
        print('Thread is running')
        lock.release()
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print('Main thread is running')

# Test threading Condition
def test_thread_condition():
    def run():
        with cond:
            cond.wait()
            print('Thread is running')
    cond = threading.Condition()
    t = threading.Thread(target=run)
    t.start()
    with cond:
        print('Main thread is running')
        cond.notify()
    t.join()

# Test threading Semaphore
def test_
