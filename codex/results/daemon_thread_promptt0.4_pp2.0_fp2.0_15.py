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

# daemon threads are killed when the main thread exits
#t.setDaemon(True)

# If a thread is a non-daemon thread, the entire Python program exits when no alive non-daemon threads are left.
# If a thread is a daemon thread, the entire Python program exits when no alive non-daemon threads are left.

# If you have a long running daemon thread, and
