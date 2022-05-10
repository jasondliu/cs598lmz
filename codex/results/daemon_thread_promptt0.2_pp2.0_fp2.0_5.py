import threading
# Test threading daemon
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

# Test threading lock
lock = threading.Lock()
def do_with_lock(lock):
    with lock:
        print 'Lock is held by {}'.format(threading.current_thread().name)

do_with_lock(lock)

# Test threading condition
class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._
