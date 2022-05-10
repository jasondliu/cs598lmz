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

print(threading.current_thread().getName(), 'Exiting')

# Test threading lock
import threading

x = 0

def increment_global():
    global x
    x += 1

def taskofThread(lock):
    for _ in range(100000):
        lock.acquire()
        increment_global()
       
