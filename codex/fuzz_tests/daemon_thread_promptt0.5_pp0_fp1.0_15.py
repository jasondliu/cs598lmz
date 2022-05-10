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
    t.join()
print('Exiting main thread')

# Test threading lock
print('\n')
lock = threading.Lock()
def worker_with_lock():
    with lock:
        print('Lock acquired via with')

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_lock)
    t.start()
    threads.append(t)
    t.join()
print('Exiting main thread')

# Test threading RLock
print('\n')
lock = threading.RLock()
def worker_with_rlock():
    with lock:
        print('Lock acquired via with')

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_rlock)
    t.start()

