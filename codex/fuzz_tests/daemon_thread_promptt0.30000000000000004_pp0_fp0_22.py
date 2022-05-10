import threading
# Test threading daemon
def daemon():
    print('Starting:', threading.currentThread().getName())
    time.sleep(2)
    print('Exiting :', threading.currentThread().getName())
    
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:', threading.currentThread().getName())
    print('Exiting :', threading.currentThread().getName())
    
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading locks
lock = threading.Lock()

def worker_with(lock):
    with lock:
        print(threading.currentThread().getName(), 'start')
        time.sleep(2)
        print(threading.currentThread().getName(), 'end')

def worker_no_with(lock):
    lock.acquire()
    try:
        print(
