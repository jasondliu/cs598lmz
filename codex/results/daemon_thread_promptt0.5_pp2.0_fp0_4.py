import threading
# Test threading daemon

def daemon():
    print('start daemon')
    time.sleep(5)
    print('end daemon')

d = threading.Thread(name = 'daemon', target = daemon)
d.setDaemon(True)

def non_daemon():
    print('start non-daemon')
    print('end non-daemon')

t = threading.Thread(name = 'non-daemon', target = non_daemon)

d.start()
t.start()

d.join()
t.join()

print('end main')

# Test threading lock

def worker_with(lock):
    with lock:
        print('lock acquired via with')

def worker_no_with(lock):
    lock.acquire()
    try:
        print('lock acquired directly')
    finally:
        lock.release()

lock = threading.Lock()
w = threading.Thread(target = worker_with, args = (lock,))
nw = threading.Thread(target = worker_no_with, args = (lock,
