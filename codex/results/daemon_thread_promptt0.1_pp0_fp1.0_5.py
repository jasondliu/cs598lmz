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
d.join()
t.join()

# Test threading lock
lock = threading.Lock()
print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))

# Test threading RLock
lock = threading.RLock()
print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))

# Test threading Semaphore
semaphore =
