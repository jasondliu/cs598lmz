import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print("Starting daemon")
        time.sleep(2)
        print("Exiting daemon")
    d = threading.Thread(name="daemon", target=daemon)
    d.setDaemon(True)
    d.start()
    d.join()

# Test threading
def test_threading():
    def worker():
        print("Starting worker")
        time.sleep(2)
        print("Exiting worker")
    t = threading.Thread(name="worker", target=worker)
    t.start()
    t.join()

# Test threading with args
def test_threading_with_args():
    def worker(num):
        print("Starting worker {}".format(num))
        time.sleep(2)
        print("Exiting worker {}".format(num))
    for i in range(5):
        t = threading.Thread(name="worker", target=worker, args=(i,))
        t.start()
        t.join()

# Test thread
