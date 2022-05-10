import threading
# Test threading daemon
def test_threading_daemon():
    def f():
        print("Threading start")
        while True:
            pass
    t = threading.Thread(target=f)
    t.setDaemon(True)
    t.start()
    print("The main thread is over")

# test_threading_daemon()

# Test threading lock
def test_threading_lock():
    lock = threading.Lock()
    def f():
        with lock:
            print("Threading start")
            while True:
                pass
    t = threading.Thread(target=f)
    t.start()
    print("The main thread is over")

# test_threading_lock()

# Test threading lock
def test_threading_rlock():
    rlock = threading.RLock()
    def f():
        with rlock:
            print("Threading start")
            while True:
                pass
    t = threading.Thread(target=f)
    t.start()
    print("The main thread is over")

