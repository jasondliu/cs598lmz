import threading
# Test threading daemon
import time

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

# Threads are non-daemon by default
# t.setDaemon(True)
# w.setDaemon(True)
# w2.setDaemon(True)

# Main thread waits for all threads to finish
# t.join()
# w.join()
# w2.join()

# Main thread exits

# If main thread exits before the other threads, they
