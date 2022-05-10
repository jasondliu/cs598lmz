import threading
# Test threading daemon

def worker():
    print("Worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Exiting")

# Test threading lock

lock = threading.Lock()

def worker_with_lock():
    lock.acquire()
    print("Worker with lock")
    lock.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_lock)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Exiting")

# Test threading RLock

lock = threading.RLock()

def worker_with_lock():
    lock.acquire()
    print("Worker with lock")
    lock.release()

threads = []
for i in range(5):
    t = thread
