import threading
# Test threading daemon

def test_threading_daemon():
    def hello():
        for i in range(5):
            print("Hello")
            time.sleep(1)

    def world():
        for i in range(5):
            print("World")
            time.sleep(1)

    t1 = threading.Thread(target=hello)
    t2 = threading.Thread(target=world)
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done")

# Test threading lock

def test_threading_lock():
    lock = threading.Lock()
    def hello():
        for i in range(5):
            lock.acquire()
            print("Hello")
            time.sleep(1)
            lock.release()

    def world():
        for i in range(5):
            lock.acquire()
            print("World")
            time.sleep(1)
            lock.release()


