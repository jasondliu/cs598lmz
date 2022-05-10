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

# Test threading with lock

lock = threading.Lock()

def worker():
    lock.acquire()
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

# Test threading with lock and condition

lock = threading.Lock()

def worker():
    with lock:
        print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.
