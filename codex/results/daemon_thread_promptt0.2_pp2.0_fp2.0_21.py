import threading
# Test threading daemon

def test_threading_daemon():
    print("Start test_threading_daemon")
    def thread_func():
        print("Start thread_func")
        time.sleep(1)
        print("End thread_func")

    t = threading.Thread(target=thread_func)
    t.setDaemon(True)
    t.start()
    print("End test_threading_daemon")

# Test threading join

def test_threading_join():
    print("Start test_threading_join")
    def thread_func():
        print("Start thread_func")
        time.sleep(1)
        print("End thread_func")

    t = threading.Thread(target=thread_func)
    t.start()
    t.join()
    print("End test_threading_join")

# Test threading join with timeout

def test_threading_join_with_timeout():
    print("Start test_threading_join_with_timeout")
    def thread_func():
        print("Start thread_func
