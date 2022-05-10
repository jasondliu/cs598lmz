import threading
# Test threading daemon

def worker():
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread())

# Test threading lock

lock = threading.Lock()

def worker_with_lock():
    lock.acquire()
    print('Lock acquired via worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker_with_lock)
    threads.append(t)
    t.start()

print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread())

# Test threading RLock

lock = threading.RLock()

def worker_with_lock():
    with lock:
        print('Lock acquired via worker')
    return

threads =
