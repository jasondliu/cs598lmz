import threading
# Test threading daemon
def worker():
    print("worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# Test threading lock
lock = threading.Lock()

def worker_with_lock():
    lock.acquire()
    print("worker_with_lock")
    lock.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_lock)
    threads.append(t)
    t.start()

# Test threading RLock
lock = threading.RLock()

def worker_with_lock():
    lock.acquire()
    print("worker_with_lock")
    lock.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_lock)
    threads.append(t)
    t.start()

# Test threading Semaphore
semaphore = threading
