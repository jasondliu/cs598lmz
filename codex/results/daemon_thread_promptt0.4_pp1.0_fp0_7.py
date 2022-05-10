import threading
# Test threading daemon

def daemon():
    print('Started')
    time.sleep(3)
    print('Exiting')

def non_daemon():
    print('Started')
    print('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non_daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock

lock = threading.Lock()

def do_this(lock):
    lock.acquire()
    try:
        print('Lock acquired in the do_this()')
    finally:
        lock.release()

def do_that(lock):
    lock.acquire()
    try:
        print('Lock acquired in the do_that()')
    finally:
        lock.release()

t1 = threading.Thread(target=do_this, args=(lock,))
t2 = threading.Thread(target=
