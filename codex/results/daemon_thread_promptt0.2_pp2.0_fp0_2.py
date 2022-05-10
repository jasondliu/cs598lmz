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

# Main thread
print(threading.currentThread().getName(), 'Starting')
time.sleep(1)
print(threading.currentThread().getName(), 'Exiting')

# Output
# MainThread Starting
# worker Starting
# Thread-1 Starting
# MainThread Exiting
# worker Exiting
# my_service Starting
# my_service Exiting
# Thread-1
