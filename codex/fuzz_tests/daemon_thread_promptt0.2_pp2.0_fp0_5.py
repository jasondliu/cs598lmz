import threading
# Test threading daemon
def test_threading_daemon():
    def thread_func():
        print('thread start')
        time.sleep(2)
        print('thread end')
    t = threading.Thread(target=thread_func)
    t.setDaemon(True)
    t.start()
    print('main thread')

# Test threading lock
def test_threading_lock():
    lock = threading.Lock()
    def thread_func():
        lock.acquire()
        print('thread start')
        time.sleep(2)
        print('thread end')
        lock.release()
    t = threading.Thread(target=thread_func)
    t.start()
    print('main thread')

# Test threading RLock
def test_threading_rlock():
    lock = threading.RLock()
    def thread_func():
        lock.acquire()
        print('thread start')
        time.sleep(2)
        print('thread end')
        lock.release()
    t = threading.Thread(target=thread_func
