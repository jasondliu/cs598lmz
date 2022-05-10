import threading
# Test threading daemon

def test_threading_daemon():
    def daemon():
        print('Start daemon')
        time.sleep(5)
        print('Stop daemon')

    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)

    def non_daemon():
        print('Start non-daemon')
        print('Stop non-daemon')

    t = threading.Thread(name='non-daemon', target=non_daemon)

    d.start()
    t.start()

    d.join()
    t.join()

test_threading_daemon()

# Test threading lock

def test_threading_lock():
    lock = threading.Lock()
    def thread_1():
        print('Thread 1 start')
        with lock:
            print('Thread 1 acquire lock')
            time.sleep(3)
        print('Thread 1 stop')

    def thread_2():
        print('Thread 2 start')
        with lock:
            print('Thread 2 acquire lock')
            time.
