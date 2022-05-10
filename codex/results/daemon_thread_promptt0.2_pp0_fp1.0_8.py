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
    print('Worker')
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
rlock = threading.RLock()

def worker_with_rlock():
    with rlock:
        print('Worker')

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_rlock
