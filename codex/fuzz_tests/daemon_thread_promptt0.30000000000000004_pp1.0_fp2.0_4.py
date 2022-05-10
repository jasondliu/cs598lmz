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
def do_this():
    with lock:
        print('Lock acquired via with')
def do_something_else():
    lock.acquire()
    try:
        print('Lock acquired directly')
    finally:
        lock.release()
t1 = threading.Thread(target=do_this)
t2 = threading.Thread(target=do_something_
