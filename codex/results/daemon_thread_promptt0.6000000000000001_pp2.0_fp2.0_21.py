import threading
# Test threading daemon
# Test threading lock

def test_lock_thread():
    lock = threading.Lock()
    print("start")
    with lock:
        print("acquire lock")
        time.sleep(5)
    print("end")

def test_lock_thread_1():
    lock = threading.Lock()
    print("start")
    with lock:
        print("acquire lock")
        time.sleep(5)
    print("end")

def test_lock_thread_2():
    lock = threading.Lock()
    print("start")
    with lock:
        print("acquire lock")
        time.sleep(5)
    print("end")

def test_lock():
    threads = []
    t = threading.Thread(target=test_lock_thread)
    t1 = threading.Thread(target=test_lock_thread_1)
    t2 = threading.Thread(target=test_lock_thread_2)
    threads.append(t)
    threads.append(t1)
    threads.append(t
