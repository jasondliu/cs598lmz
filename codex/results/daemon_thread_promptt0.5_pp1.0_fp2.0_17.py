import threading
# Test threading daemon
def test_threading_daemon():
    print("Start Main Thread...")
    t = threading.Thread(target=test_threading, args=("test_threading_daemon",))
    t.setDaemon(True)
    t.start()
    t.join()
    print("End Main Thread...")

# Test threading
def test_threading(name):
    print("Start Thread " + name + "...")
    time.sleep(2)
    print("End Thread " + name + "...")

# Test threading lock
def test_threading_lock():
    print("Start Main Thread...")
    lock = threading.Lock()
    for i in range(5):
        t = threading.Thread(target=test_threading_lock_sub, args=(i, lock))
        t.start()
    print("End Main Thread...")

def test_threading_lock_sub(num, lock):
    lock.acquire()
    print("Lock Sub Thread " + str(num) + "...")
    time.sleep
