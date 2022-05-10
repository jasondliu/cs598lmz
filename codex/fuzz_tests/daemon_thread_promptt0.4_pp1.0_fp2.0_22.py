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

#t.join()
#w.join()
#w2.join()

print("Done")

# Output:
# worker Starting
# worker Exiting
# Thread-1 Starting
# Thread-1 Exiting
# my_service Starting
# my_service Exiting
# Done

# If daemon=True, the thread will be killed as soon as the main thread exits.

