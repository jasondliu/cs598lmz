import threading
# Test threading daemon
def test_threading_daemon():
    def f():
        print("f")
        print("f end")
    print("main start")
    t = threading.Thread(target=f)
    t.setDaemon(True)
    t.start()
    print("main end")

# Test threading lock
def test_threading_lock():
    lock = threading.Lock()
    def f():
        lock.acquire()
        print("f")
        lock.release()
        print("f end")
    print("main start")
    t = threading.Thread(target=f)
    t.setDaemon(True)
    t.start()
    print("main end")

# Test threading lock
def test_threading_lock_with():
    lock = threading.Lock()
    def f():
        with lock:
            print("f")
        print("f end")
    print("main start")
    t = threading.Thread(target=f)
    t.setDaemon(True)
    t.start()
