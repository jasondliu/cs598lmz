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
# lock = threading.Lock()
# lock.acquire()
# lock.release()

# Test threading RLock
# rlock = threading.RLock()
# rlock.acquire()
# rlock.release()

# Test threading Semaphore
# semaphore = threading.Semaphore(5)
# semaphore.acquire()
# semaphore.release()

# Test threading BoundedSemaphore
# bsemaphore = threading.BoundedSemaphore(5)
# bsemaphore.acquire()
# bsemaphore.release()

# Test threading Condition
# condition = threading.Condition()

