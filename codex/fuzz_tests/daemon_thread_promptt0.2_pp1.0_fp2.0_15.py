import threading
# Test threading daemon
def daemon():
    print('Starting:')
    time.sleep(2)
    print('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:')
    print('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading join
def worker():
    """thread worker function"""
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

# Test threading lock
lock = threading.Lock()

def worker_with(lock):
    with lock:
        print('Lock acquired via with')

def worker_no_with(lock):
    lock.acquire()
    try:
        print('
