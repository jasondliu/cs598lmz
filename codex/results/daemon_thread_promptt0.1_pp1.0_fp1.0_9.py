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

# Test threading lock
lock = threading.Lock()

def do_with_lock(lock):
    with lock:
        print('Lock is held by {}'.format(threading.current_thread().name))

def do_without_lock(lock):
    print('Lock is held by {}'.format(threading.current_thread().name))

def do_with_lock_2(lock):
    with lock:
        print('Lock is
