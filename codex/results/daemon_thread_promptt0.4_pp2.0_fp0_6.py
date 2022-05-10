import threading
# Test threading daemon
def test_threading():
    def test():
        while True:
            print("test")
            time.sleep(1)
    t = threading.Thread(target=test)
    t.setDaemon(True)
    t.start()
    print("test threading daemon")
    time.sleep(3)
    print("test threading daemon end")

# Test threading lock
def test_threading_lock():
    lock = threading.Lock()
    def test():
        lock.acquire()
        print("test")
        lock.release()
    t = threading.Thread(target=test)
    t.start()
    t.join()
    print("test threading lock")

# Test threading queue
def test_threading_queue():
    q = queue.Queue()
    def test():
        while True:
            print(q.get())
    t = threading.Thread(target=test)
    t.setDaemon(True)
    t.start()
    print("test threading queue")
    q.put("
