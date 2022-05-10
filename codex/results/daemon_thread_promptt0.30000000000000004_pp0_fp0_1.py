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
def do_with_lock(lock):
    with lock:
        print('Lock is held by', threading.current_thread().name)

t1 = threading.Thread(target=do_with_lock, args=(lock,))
t2 = threading.Thread(target=do_with_lock, args=(lock,))
t1.
