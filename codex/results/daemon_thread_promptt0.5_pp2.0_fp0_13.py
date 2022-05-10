import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(0.2)
    print(threading.currentThread().getName(), 'Exiting')

def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(0.3)
    print(threading.currentThread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
#w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

#w.join()
#w2.join()
#t.join()

# The daemon threads will automatically exit when all non-daemon threads finish.
# https://docs.python.org/3/library/threading.html
# If you want to wait for all threads to finish
