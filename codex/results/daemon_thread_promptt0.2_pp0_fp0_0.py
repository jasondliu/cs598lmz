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

print('Finished')

# Test threading with lock
lock = threading.Lock()

def worker_with_lock():
    lock.acquire()
    print('Lock acquired via worker')
    lock.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_lock)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Finished')

# Test threading with lock and condition
lock = threading.Lock()

def worker_with_lock_and_condition():
    with lock:
        print('Lock acquired via worker')

threads = []
for i in range(5):
    t = threading.Thread(target
