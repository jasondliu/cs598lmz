import threading
# Test threading daemon mode
# https://stackoverflow.com/questions/190010/daemon-threads-explanation
def test_threading_daemon_mode():
    class TestThread(threading.Thread):
        def run(self):
            print("Thread started!")
            while True:
                pass

    thread = TestThread()
    thread.setDaemon(True)
    thread.start()
    print("Main thread ends!")

# Test threading Lock
# https://docs.python.org/3/library/threading.html#lock-objects
def test_threading_lock():
    class TestThread(threading.Thread):
        lock = threading.Lock()
        def run(self):
            TestThread.lock.acquire()
            print("Thread %d" % self.getName())
            TestThread.lock.release()

    for i in range(10):
        thread = TestThread()
        thread.start()

# Test threading Semaphore
# https://docs.python.org/3/library/threading.html#semaphore-
