import threading
# Test threading daemon
def test_threading_daemon():
    def worker():
        for i in range(3):
            print("i am a worker")
            time.sleep(1)
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    print("main thread")
# test_threading_daemon()

# Threading lock
def test_threading_lock():
    lock = threading.Lock()
    def worker():
        while True:
            lock.acquire()
            print("I am a worker")
            lock.release()
            time.sleep(1)

    t1 = threading.Thread(target=worker)
    t2 = threading.Thread(target=worker)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# test_threading_lock()

# Test threading semaphore
def test_threading_semaphore():
    sem = threading.Semaphore(2)
    def worker():
        sem
