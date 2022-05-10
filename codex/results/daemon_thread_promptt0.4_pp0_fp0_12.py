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

# The following is the output of the example:
#
# worker Starting
# worker Exiting
# Thread-1 Starting
# worker Starting
# Thread-1 Exiting
# worker Exiting
# my_service Starting
# my_service Exiting

# As expected, the daemon thread my_service is killed when the main thread exits.

# If you want a thread to be a daemon, you just have to
