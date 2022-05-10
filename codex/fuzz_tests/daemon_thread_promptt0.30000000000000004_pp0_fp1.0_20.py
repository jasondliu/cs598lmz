import threading
# Test threading daemon
def worker():
    print('worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Exiting main thread')

# Test threading non-daemon
def worker():
    print('worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Exiting main thread')

# Test threading lock
lock = threading.Lock()

def worker_with(lock):
    lock.acquire()
    print('Lock acquired via with')
    lock.release()

def worker_no_with(lock):
    lock.acquire()
    print('Lock acquired directly')
    lock.release()

worker_with(
