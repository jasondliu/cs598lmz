import threading
# Test threading daemon
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

# Main thread
print(threading.current_thread().name, 'Starting')
time.sleep(0.1)
print(threading.current_thread().name, 'Exiting')

# Threading daemon
t.setDaemon(True)
w.setDaemon(True)
w2.setDaemon(True)

# Test threading join
t
