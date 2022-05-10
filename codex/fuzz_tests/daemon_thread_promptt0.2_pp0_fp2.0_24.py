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

print('Finished')

# Test threading lock
lock = threading.Lock()

def do_with_lock(lock):
    with lock:
        print('Lock is held')

lock.acquire()
print('Lock is held')
lock.release()
print('Lock is released')

lock = threading.Lock()

def worker_with(lock):
    with lock:
       
