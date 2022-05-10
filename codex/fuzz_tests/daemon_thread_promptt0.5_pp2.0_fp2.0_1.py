import threading
# Test threading daemon
def test_threading_daemon():
    def worker():
        print("worker")
        time.sleep(1)
        print("worker")
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# test_threading_daemon()
# Test threading join
def test_threading_join():
    def worker():
        print("worker")
        time.sleep(1)
        print("worker")
    t = threading.Thread(target=worker)
    t.start()
    t.join()
    print("main thread")

# test_threading_join()
# Test threading Lock
def test_threading_lock():
    count = 0
    lock = threading.Lock()
    def worker():
        nonlocal count
        for i in range(1000000):
            lock.acquire()
            count += 1
            lock.release()
    t1 = threading.Thread(target=worker)
    t2 = threading.Thread(target=worker)
    t1.start
