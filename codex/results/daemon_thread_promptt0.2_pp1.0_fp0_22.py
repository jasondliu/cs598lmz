import threading
# Test threading daemon

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

# The daemon thread will quit immediately when the main thread exits.
# A daemon thread will quit when there is only daemon threads left.
t.setDaemon(True)
w.setDaemon(True)

# The daemon threads exist as long as the program runs.
# The non-daemon threads are used to do some tasks.
# The program will quit when all non-daemon threads exit.

#
