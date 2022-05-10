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

print(threading.currentThread().getName(), 'Exiting')

# The daemon thread will exit when the main thread exits.
# The non-daemon thread will continue to run until it exits.

# Output:
# MainThread Starting
# MainThread Exiting
# worker Starting
# worker Exiting
# Thread-1 Starting
# Thread-1 Exiting
# my_service Starting
