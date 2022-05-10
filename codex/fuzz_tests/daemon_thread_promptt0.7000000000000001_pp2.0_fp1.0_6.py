import threading
# Test threading daemonic
print(threading.current_thread().name)
print(threading.current_thread().daemon)

# The main thread always exits when there are no more non-daemon threads
def worker():
    print(threading.current_thread().name, 'Starting')
    time.sleep(0.2)
    print(threading.current_thread().name, 'Exiting')

def my_service():
    print(threading.current_thread().name, 'Starting')
    time.sleep(0.3)
    print(threading.current_thread().name, 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

# The whole program exits when the main thread exits.
# If a daemon thread creates a non-daemon thread, the non-daemon thread will not stop the program from exiting.

#
