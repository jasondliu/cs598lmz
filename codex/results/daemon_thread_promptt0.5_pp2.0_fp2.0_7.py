import threading
# Test threading daemon.
# Using a threading.Thread() instance
# to create a daemon thread.
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

# Test threading daemon.
# Using a threading.Thread() instance
# to create a daemon thread.
def daemon():
    print 'Starting:', threading.currentThread().getName()
    time.sleep(2)
    print 'Exiting :', threading.currentThread().getName()
d = threading.Thread(name='daemon
