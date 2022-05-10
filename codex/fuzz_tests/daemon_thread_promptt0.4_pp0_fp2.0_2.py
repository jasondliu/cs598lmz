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
def worker():
    print(threading.current_thread().name, 'Starting')
    time.sleep(0.2)
    print(threading.current_thread().name, 'Exiting')

def my_service():
    print(threading.current_thread().name, 'Starting')
    time.sleep(0.3)
    print(threading.current_thread().name, 'Exiting')

t =
