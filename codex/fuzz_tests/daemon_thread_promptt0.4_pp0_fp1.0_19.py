import threading
# Test threading daemon

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

# Test threading with lock

lock = threading.Lock()

def worker():
    lock.acquire()
    print('Worker')
    lock.release()
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Exiting')

# Test threading with lock and queue

lock = threading.Lock()

def worker():
    lock.acquire()
    print('Worker')
    lock.release()
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
