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

# daemon threads
# http://stackoverflow.com/questions/190010/daemon-threads-explanation
# http://stackoverflow.com/questions/16672451/what-is-the-difference-between-a-daemon-thread-and-a-normal-thread-in-python
# http://stackoverflow.com/questions/16688888/
