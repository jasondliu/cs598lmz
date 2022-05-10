import threading
# Test threading daemon
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)
t = threading.Thread(name='non-daemon', target=non_daemon)
d.start()
t.start()
d.join()
t.join()

# Test threading lock
lock = threading.Lock()
def worker_with(lock):
    with lock:
        print(threading.current_thread().name, 'Started')
        time.sleep(0.2)
        print(threading.current_thread().name, 'Exiting')
def worker_no_with(lock):
    lock.acquire()
    try:
        print(threading.current_
