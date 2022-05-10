import threading
# Test threading daemon
def worker():
    print "Worker"
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
print "Done"

# Test lock
lock = threading.Lock()

def worker():
    lock.acquire()
    print "Worker"
    lock.release()


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
print "Done"


# Test semaphore
semaphore = threading.Semaphore(0)

def worker():
    semaphore.acquire()
    print "Worker"
    semaphore.release()

threads = []
for i in range(5):
    t = threading
