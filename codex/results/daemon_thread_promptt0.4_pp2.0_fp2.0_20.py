import threading
# Test threading daemon

def worker():
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print 'Exiting Main Thread'

def worker():
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()
    threads.append(t)

print 'Exiting Main Thread'

# Test threading lock

lock = threading.Lock()

def worker_with(lock):
    lock.acquire()
    print 'Lock acquired via with'
    lock.release()

def worker_no_with(lock):
    lock.acquire()
    print 'Lock acquired directly'
    lock.release()

worker_with(lock)
worker_no_with(lock)

# Test threading r
