import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(2)
    print('Exit daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start non-daemon')
    print('Exit non-daemon')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading
def worker():
    """thread worker function"""
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# Test threading lock
lock = threading.Lock()

def worker_with(lock):
    with lock:
        print('Lock acquired via with')

def worker_no_with(lock):
    lock.acquire()
    try:

