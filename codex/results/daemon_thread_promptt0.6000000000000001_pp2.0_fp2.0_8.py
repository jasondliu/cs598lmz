import threading
# Test threading daemon
# The parent thread will exit immediately after the creation of a daemon thread,
# regardless of whether the daemon thread is still running or not.

def worker():
    print threading.current_thread().name, 'Starting'
    time.sleep(2)
    print threading.current_thread().name, 'Exiting'

def my_service():
    print threading.current_thread().name, 'Starting'
    time.sleep(5)
    print threading.current_thread().name, 'Exiting'

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(name='worker2', target=worker)

##t.setDaemon(True)  # If daemon thread is set, the parent thread will exit immediately after the creation of a daemon thread, regardless of whether the daemon thread is still running or not.
w.setDaemon(True)
w2.setDaemon(True)

t.start()
w.start()
w2.start()
