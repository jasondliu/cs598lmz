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

# Above, my_service is the daemon thread, which will be terminated once the main thread is completed.
# The worker and worker2 are non-daemon threads, which will be terminated after the daemon thread is terminated.
# If you comment out the daemon thread, the program will be blocked until the non-daemon thread is finished.
# So you can use daemon thread to control the whole program.

# The following is a
