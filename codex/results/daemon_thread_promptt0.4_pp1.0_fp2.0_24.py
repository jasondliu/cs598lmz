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
    print('Lock acquired via worker')

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_lock)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Exiting')

# Test threading rlock
rlock = threading.RLock()

def worker_with_rlock():
    rlock.acquire()
    print('RLock acquired via worker')

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_r
