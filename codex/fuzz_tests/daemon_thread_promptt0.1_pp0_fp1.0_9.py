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

def worker_with(lock):
    with lock:
        print('Lock acquired via with')

def worker_no_with(lock):
    lock.acquire()
    try:
        print('Lock acquired directly')
    finally:
        lock.release()

w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()

# Test threading rlock
rlock = threading.RLock()

def worker_with(lock):
    with lock:
        print('Lock acquired via with')

def worker_no_with(lock
