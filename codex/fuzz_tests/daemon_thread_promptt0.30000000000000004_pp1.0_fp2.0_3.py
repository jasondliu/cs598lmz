import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(5)
    print('End daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start non-daemon')
    print('End non-daemon')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
lock = threading.Lock()

def do_this():
    while True:
        lock.acquire()
        try:
            print('Lock acquired in the do_this()')
        finally:
            lock.release()

def do_that():
    while True:
        lock.acquire()
        try:
            print('Lock acquired in the do_that()')
        finally:
            lock.release()

t1 = threading.Thread(target=do_this)
t2 = threading
