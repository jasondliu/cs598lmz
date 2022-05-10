import threading
# Test threading daemon
def worker():
    print('worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# Test threading lock
lock = threading.Lock()
lock.acquire()
lock.release()

# Test threading RLock
rlock = threading.RLock()
rlock.acquire()
rlock.release()

# Test threading Condition
condition = threading.Condition()
condition.acquire()
condition.release()

# Test threading Event
event = threading.Event()
event.set()
event.clear()

# Test threading Timer
timer = threading.Timer(1, worker)
timer.start()
timer.cancel()

# Test threading Barrier
barrier = threading.Barrier(5)
barrier.wait()

# Test threading Semaphore
semaphore = threading.Semaphore(5)
semaphore.acquire()
semaphore.release()
