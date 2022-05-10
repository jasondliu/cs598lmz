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

for thread in threads:
    thread.join()

print 'Exiting Main Thread'

# Test threading lock

lock = threading.Lock()

def worker():
    print 'Worker'
    lock.acquire()
    print 'Lock acquired via worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print 'Exiting Main Thread'

# Test threading RLock

lock = threading.RLock()

def worker():
    print 'Worker'
    lock.acquire()
    print 'Lock acquired via worker'
    return

threads = []
for i in range(5):
    t = thread
