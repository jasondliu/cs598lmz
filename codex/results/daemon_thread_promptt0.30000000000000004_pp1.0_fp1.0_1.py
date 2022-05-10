import threading
# Test threading daemon
def daemon():
    print('Starting:', threading.currentThread().getName())
    time.sleep(2)
    print('Exiting :', threading.currentThread().getName())

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:', threading.currentThread().getName())
    print('Exiting :', threading.currentThread().getName())

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading lock
lock = threading.Lock()
print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))

# Test threading RLock
lock = threading.RLock()
print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))

# Test threading Semaphore
semaphore = threading.Semaphore(2)

