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

for thread in threads:
    thread.join()

print("Done")

# Test threading with locks

lock = threading.Lock()

def worker_with_lock():
    lock.acquire()
    print("Lock acquired")
    lock.release()

threads = []

for i in range(5):
    t = threading.Thread(target=worker_with_lock)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Done")

# Test threading with locks and condition

lock = threading.Lock()

def worker_with_lock():
    with lock:
        print("Lock acquired")

threads = []

for i in range(5):
    t = threading.Thread(target=worker_with
