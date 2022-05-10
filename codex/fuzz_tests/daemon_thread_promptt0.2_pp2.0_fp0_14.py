import threading
# Test threading daemon
def test_daemon():
    print("start")
    time.sleep(2)
    print("end")

d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

d.start()
d.join()

print("main thread end")

# Test threading lock
lock = threading.Lock()
def test_lock():
    lock.acquire()
    print("start")
    time.sleep(2)
    print("end")
    lock.release()

d = threading.Thread(name='daemon', target=test_lock)
d.setDaemon(True)

d.start()
d.join()

print("main thread end")

# Test threading RLock
lock = threading.RLock()
def test_lock():
    lock.acquire()
    print("start")
    time.sleep(2)
    print("end")
    lock.release()

d = threading.Thread(name='daemon', target=test_lock)
d
