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

# daemon thread
d = threading.Thread(name='daemon', target=worker)
d.setDaemon(True)
d.start()

# main thread
print threading.currentThread().getName(), 'Exiting'

# main thread is not a daemon thread, so it will wait for all non-daemon threads to exit
# daemon thread will exit when the main thread exits

# output
