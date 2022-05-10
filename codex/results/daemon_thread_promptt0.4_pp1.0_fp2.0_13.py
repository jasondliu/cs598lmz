import threading
# Test threading daemon

def worker():
    print('worker')
    sys.exit()

thread = threading.Thread(target=worker)
thread.daemon = True
thread.start()

time.sleep(0.1)
print('main thread')

# Test threading join

def worker():
    print('worker')
    time.sleep(0.1)
    print('worker again')

thread = threading.Thread(target=worker)
thread.start()
thread.join()

print('main thread')

# Test threading queue

def worker(queue):
    queue.put('foo')

queue = Queue.Queue()
thread = threading.Thread(target=worker, args=(queue,))
thread.start()
print(queue.get())
print('main thread')

# Test threading lock

lock = threading.Lock()

def worker_with(lock):
    with lock:
        print('lock acquired via with')

def worker_no_with(lock):
    lock.acquire()
    try:
        print('lock acquired
