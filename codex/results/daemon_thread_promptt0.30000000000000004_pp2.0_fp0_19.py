import threading
# Test threading daemon
def test_threading_daemon():
    def worker():
        print("worker")
        time.sleep(1)
        print("worker")
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()
    print("main thread")

# Test threading lock
def test_threading_lock():
    lock = threading.Lock()
    def worker():
        print("worker")
        time.sleep(1)
        print("worker")
    t = threading.Thread(target=worker)
    t.start()
    print("main thread")

# Test threading rlock
def test_threading_rlock():
    lock = threading.RLock()
    def worker():
        print("worker")
        time.sleep(1)
        print("worker")
    t = threading.Thread(target=worker)
    t.start()
    print("main thread")

# Test threading condition
def test_threading_condition():
    lock = threading.Condition()
    def worker():
