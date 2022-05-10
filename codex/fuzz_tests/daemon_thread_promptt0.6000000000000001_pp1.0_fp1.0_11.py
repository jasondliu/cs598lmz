import threading
# Test threading daemon

def worker():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'Exiting')

def my_service():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.3)
    print(threading.current_thread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

#t.join()

# Output:
# worker Starting
# Thread-1 Starting
# my_service Starting
# worker Exiting
# Thread-1 Exiting
# my_service Exiting

# If we uncomment the t.join() we get the following output:
# worker Starting
# Thread-1 Starting
# my_service Starting
#
