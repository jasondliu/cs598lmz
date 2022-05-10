import threading
# Test threading daemon
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading join
import time
import threading

def worker():
    """thread worker function"""
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

def my_service():
    """thread worker function"""
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print
