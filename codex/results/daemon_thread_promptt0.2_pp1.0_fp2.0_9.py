import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print("Start")
        time.sleep(2)
        print("End")

    d = threading.Thread(name="daemon", target=daemon)
    d.setDaemon(True)
    d.start()
    d.join()

# Test threading lock
def test_threading_lock():
    lock = threading.Lock()
    def worker_with(lock):
        with lock:
            print(threading.current_thread().name, "Start")
            time.sleep(2)
            print(threading.current_thread().name, "End")

    def worker_no_with(lock):
        lock.acquire()
        print(threading.current_thread().name, "Start")
        time.sleep(2)
        print(threading.current_thread().name, "End")
        lock.release()

    w = threading.Thread(target=worker_with, args=(lock,))
    nw = threading.Thread(target=worker_no_with
