import threading
# Test threading daemon:
def test_threading_daemon():
    t = threading.Thread(target=thread_func)
    t.setDaemon(True)
    t.start()
    t.join()


def thread_func():
    print("Started thread")
    time.sleep(3)
    print("Finished thread")


# Test threading daemon:
def test_threading_daemon2():
    t = threading.Thread(target=thread_func2)
    t.setDaemon(True)
    t.start()
    print("Main thread")
    time.sleep(0.6)
    print("Still main thread")


def thread_func2():
    print("Started thread")
    time.sleep(3)
    print("Finished thread")


# Test threading daemon:
def test_threading_daemon3():
    t = threading.Thread(target=thread_func3)
    t.setDaemon(True)
    t.start()
    t.join()
    print("Main thread")
    time.sleep
