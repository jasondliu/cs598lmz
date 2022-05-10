import threading
# Test threading daemon

def worker():
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Exiting')

# Test threading lock

lock = threading.Lock()

def worker_with_lock():
    lock.acquire()
    print('Lock acquired via with')
    lock.release()

def worker_no_with():
    lock.acquire()
    print('Lock acquired directly')
    lock.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_lock)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Exiting')

# Test threading RLock

lock = threading.RLock()

def worker_with_lock():
    with lock:
        print('Lock acquired
