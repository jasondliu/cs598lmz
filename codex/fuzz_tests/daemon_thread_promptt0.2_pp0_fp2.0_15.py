import threading
# Test threading daemon

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

# t.join()
# w.join()
# w2.join()

print(threading.currentThread().getName(), 'Exiting')

# If a thread is a daemon thread, it will exit when the main program exits.
# If a thread is not a daemon thread, it will exit when the main program exits.
# If a thread is a daemon thread, it will exit when
