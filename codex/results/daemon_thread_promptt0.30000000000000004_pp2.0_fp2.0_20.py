import threading
# Test threading daemon

def worker():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

def my_service():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(3)
    print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

# t.join()
# w.join()
# w2.join()

print "Exiting main thread"

# t.join()
# w.join()
# w2.join()

# Exiting main thread
# worker Starting
# worker Exiting
# worker Starting
# worker Exiting
# my_service Starting
# my_service Exiting

# Exiting main thread

