import threading
# Test threading daemon
import time

def worker():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

def my_service():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(3)
    print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='my_service', target=my_service)
# Set the thread daemon to True
w = threading.Thread(name='worker', target=worker)
# Set the thread daemon to False
w2 = threading.Thread(name='worker2', target=worker)

w.setDaemon(True)
w2.setDaemon(False)
t.start()
w.start()
w2.start()

# Main thread exit

# Main thread exit

# Main thread exit
