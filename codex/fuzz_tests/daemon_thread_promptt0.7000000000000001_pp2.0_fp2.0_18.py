import threading
# Test threading daemon
def my_daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)
d = threading.Thread(name='my_daemon', target=my_daemon)
d.setDaemon(True)
def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)
t = threading.Thread(name='non_daemon', target=non_daemon)
t.setDaemon(False)
d.start()
t.start()
d.join()
t.join()

# Test lock
lock = threading.Lock()
def func_with_lock(i):
    lock.acquire()
    print('{} got lock {}'.format(threading.current_thread().name, i))
    time.sleep(.5)
    print('{} releasing {}'.format(threading.current_thread().name, i))
   
