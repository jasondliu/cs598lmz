import threading
# Test threading daemon

def test_thread_daemon():
    print('test_thread_daemon')
    def func():
        print('func')
        while True:
            time.sleep(1)
            print('func sleep 1')
    t = threading.Thread(target=func)
    t.setDaemon(True)
    t.start()
    print('test_thread_daemon end')

# test_thread_daemon()

# Test threading lock

def test_thread_lock():
    print('test_thread_lock')
    lock = threading.Lock()
    def func():
        print('func')
        lock.acquire()
        print('func acquire lock')
        time.sleep(1)
        lock.release()
        print('func release lock')
    t = threading.Thread(target=func)
    t.start()
    t.join()
    print('test_thread_lock end')

# test_thread_lock()

# Test threading condition

def test_thread_condition():
    print('test_thread_
