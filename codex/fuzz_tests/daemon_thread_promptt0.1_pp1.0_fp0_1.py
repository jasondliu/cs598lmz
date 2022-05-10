import threading
# Test threading daemon
def daemon():
    print('Start:', threading.current_thread().name)
    time.sleep(2)
    print('End:', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start:', threading.current_thread().name)
    print('End:', threading.current_thread().name)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading lock
lock = threading.Lock()
def do_this(lock):
    lock.acquire()
    try:
        print('Lock acquired in', threading.current_thread().name)
    finally:
        lock.release()

def do_after(lock):
    print('Lock released in', threading.current_thread().name)

t1 = threading.Thread(target=do_this, args=(lock,))
t
