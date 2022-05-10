import threading
# Test threading daemon

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
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

# daemon thread
d = threading.Thread(name='daemon', target=my_service)
d.setDaemon(True)
d.start()

# wait for all threads to finish
t.join()
w.join()
w2.join()
d.join()

print('Exiting main thread')

# Output:
#
# worker
