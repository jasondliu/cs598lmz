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

# Sample output
'''
my_service Starting
worker Starting
Thread-1 Starting
my_service Exiting
worker Exiting
Thread-1 Exiting
'''

# The main thread creates a new thread, and then exits.
# The new thread is a daemon thread. When the main thread exits, no thread is left in the program. Since there is no
# thread, the daemon thread exits too.


