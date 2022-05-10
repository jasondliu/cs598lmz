import threading
# Test threading daemon
#
def worker():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

def my_service():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(3)
    print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

#
# Test threading lock
#
lock = threading.Lock()

def worker_with(lock):
    with lock:
        print threading.currentThread().getName()
        time.sleep(3)
    print threading.currentThread().getName(), 'done'

def worker_no_with(lock):
    lock.acquire()
    try:
        print thread
