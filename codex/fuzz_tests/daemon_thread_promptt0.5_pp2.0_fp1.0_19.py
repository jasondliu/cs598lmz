import threading
# Test threading daemon
def test_threading_daemon():
    def run():
        print("Starting a thread")
        time.sleep(1)
        print("Ending a thread")
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    print("Main thread")

# Test threading with wait
def test_threading_wait():
    def run():
        print("Starting a thread")
        time.sleep(1)
        print("Ending a thread")
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("Main thread")

# Test threading with wait and daemon
def test_threading_wait_daemon():
    def run():
        print("Starting a thread")
        time.sleep(1)
        print("Ending a thread")
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    t.join()
    print("Main thread")

# Test threading with
