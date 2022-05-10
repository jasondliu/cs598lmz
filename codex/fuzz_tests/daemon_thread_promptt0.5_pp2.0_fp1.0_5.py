import threading
# Test threading daemon
def threading_daemon():
    print('start daemon')
    time.sleep(2)
    print('end daemon')

d = threading.Thread(name='daemon', target=threading_daemon)
d.setDaemon(True)

def non_daemon():
    print('start non-daemon')
    print('end non-daemon')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading
def threading_test():
    print('hello world')

t = threading.Thread(name='threading_test', target=threading_test)
t.start()
t.join()

print('main thread')

# Test threading lock
lock = threading.Lock()

def threading_lock():
    lock.acquire()
    try:
        print('hello world')
    finally:
        lock.release()

t = threading.Thread(name='
