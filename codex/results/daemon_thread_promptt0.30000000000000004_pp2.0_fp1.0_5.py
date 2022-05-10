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

print('Done')

# Test Threading Lock

lock = threading.Lock()

def worker_with_lock(i):
    lock.acquire()
    print('Worker: %d' % i)
    lock.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_lock, args=(i,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Done')

# Test Threading RLock

lock = threading.RLock()

def worker_with_lock(i):
    lock.acquire()
    print('Worker: %d' % i)
    lock.release()

threads
