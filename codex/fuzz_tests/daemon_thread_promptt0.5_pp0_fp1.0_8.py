import threading
# Test threading daemon
def daemon():
    print('Start: %s' % threading.current_thread().name)
    time.sleep(2)
    print('End: %s' % threading.current_thread().name)

def non_daemon():
    print('Start: %s' % threading.current_thread().name)
    print('End: %s' % threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# d.join()
t.join()

# Test threading lock
lock = threading.Lock()

def thread_1():
    lock.acquire()
    print('Thread 1 is running')
    time.sleep(2)
    print('Thread 1 is ending')
    lock.release()

def thread_2():
    lock.acquire()
    print('Thread 2 is running')
   
