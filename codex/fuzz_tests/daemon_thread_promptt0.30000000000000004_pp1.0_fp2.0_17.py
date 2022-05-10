import threading
# Test threading daemon
def test_thread():
    print("Test thread")
    time.sleep(1)
    print("Test thread end")

# Test threading daemon
def test_thread_daemon():
    print("Test thread daemon")
    time.sleep(1)
    print("Test thread daemon end")

# Test threading
def test_threading():
    print("Test threading")
    t = threading.Thread(target=test_thread)
    t.start()
    print("Test threading end")

# Test threading daemon
def test_threading_daemon():
    print("Test threading daemon")
    t = threading.Thread(target=test_thread_daemon)
    t.daemon = True
    t.start()
    print("Test threading daemon end")

# Test threading daemon
def test_threading_daemon_join():
    print("Test threading daemon join")
    t = threading.Thread(target=test_thread_daemon)
    t.daemon = True
    t.start()
    t.join()
