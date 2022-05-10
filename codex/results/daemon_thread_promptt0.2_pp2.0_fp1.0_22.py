import threading
# Test threading daemon
import time

def worker():
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Exiting')

# Test threading lock
lock = threading.Lock()

def worker():
    lock.acquire()
    print('Worker')
    lock.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Exiting')

# Test threading RLock
lock = threading.RLock()

def worker():
    lock.acquire()
    print('Worker')
    lock.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()

