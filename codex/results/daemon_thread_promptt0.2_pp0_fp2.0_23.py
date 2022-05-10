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
    t.join()

print('Exiting Main Thread')

# Test threading with lock

lock = threading.Lock()

def worker():
    print('Worker')
    lock.acquire()
    print('Lock acquired by', threading.current_thread().name)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
    t.join()

print('Exiting Main Thread')

# Test threading with lock and release

lock = threading.Lock()

def worker():
    print('Worker')
    lock.acquire()
    print('Lock acquired by', threading.current_thread().name)
    lock.release()
    print('Lock released by', threading.current
