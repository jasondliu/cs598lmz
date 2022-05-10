import threading
# Test threading daemonic threads
import time

class Worker(threading.Thread):
    def run(self):
        print(threading.currentThread().getName(), 'Starting')
        time.sleep(0.2)
        print(threading.currentThread().getName(), 'Exiting')

def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(0.3)
    print(threading.currentThread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = Worker()
w2 = Worker()
w.start()
w2.start()
t.start()
