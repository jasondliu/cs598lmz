import threading
# Test threading daemon mode
def worker():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.1)
    print(threading.current_thread().getName(), 'Exiting')

def my_service():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()
w.join()
w2.join()

"""
When Daemon mode worker thread done => program done
"""
# use daemon mode
w = threading.Thread(name='daemon worker', target=worker)
w.setDaemon(True)
w.start()

# >>> t = threading.Thread(name='non-daemon', target
