import threading
# Test threading daemon
#
# A daemon thread will shut down immediately when the program exits.
# If not set daemon, the program will wait for all non-daemon threads
# to exit before it does.

def worker():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

def my_service():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(3)
    print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

# main thread
print threading.currentThread().getName(), 'Starting'
t.join()
print threading.currentThread().getName(), 'Exiting'
