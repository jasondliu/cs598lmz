import threading
# Test threading daemon

def test_threading_daemon():
    """
    A test for threading daemon
    """
    def test_thread():
        """
        Sub thread function
        """
        print("I'm sub thread")
        time.sleep(1)
        print("Sub thread done")

    print("Main thread start")
    thread = threading.Thread(target=test_thread)
    thread.daemon = True
    thread.start()
    print("Main thread done")


test_threading_daemon()

# Test threading lock

def test_threading_lock():
    """
    Test threading lock
    """
    lock = threading.Lock()

    def test_thread():
        """
        Sub thread function
        """
        print("Sub thread start")
        lock.acquire()
        global num
        num += 1
        lock.release()
        print("Sub thread done")

    num = 0
    thread_list = []
    for i in range(100):
        thread_list.append(threading.Thread(target=test_thread
