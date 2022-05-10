import threading
# Test threading daemon.
def daemon():
    print 'Starting:', threading.currentThread().getName()
    time.sleep(2)
    print 'Exiting :', threading.currentThread().getName()

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print 'Starting:', threading.currentThread().getName()
    print 'Exiting :', threading.currentThread().getName()

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock.
lock = threading.Lock()
def my_lock():
    lock.acquire()
    try:
        print 'Lock acquired.'
        time.sleep(2)
    finally:
        lock.release()
        print 'Lock released.'

t = threading.Thread(target=my_lock)
t.start()
t.join()

# Test threading
