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

print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread())

# Test threading lock
lock = threading.Lock()
lock.acquire()
lock.release()

# Test threading rlock
rlock = threading.RLock()
rlock.acquire()
rlock.release()

# Test threading condition
con = threading.Condition()
con.acquire()
con.release()

# Test threading semaphore
sem = threading.Semaphore(3)
sem.acquire()
sem.release()

# Test threading barrier
bar = threading.Barrier(3)
bar.wait()

# Test threading event
event = threading.Event()
event.set()
event.clear()
event.wait()

#
