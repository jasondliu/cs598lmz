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

for t in threads:
    t.join()

print 'Exiting Main Thread'

# Test threading lock

lock = threading.Lock()

def worker():
    with lock:
        print 'Lock acquired via with'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t
