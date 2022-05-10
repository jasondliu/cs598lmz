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

# Test threading lock
def worker_with(lock):
    with lock:
        print(threading.current_thread().getName(), 'Starting')
        time.sleep(2)
        print(threading.current_thread().getName(), 'Exiting')

def worker_no_with(lock):
    lock.acquire()
    try:
        print(threading.current_thread().getName(), 'Starting')
        time.sleep(2)
        print(threading.current_thread().getName(), 'Exiting')
    finally:
        lock.release()

lock = threading.Lock
