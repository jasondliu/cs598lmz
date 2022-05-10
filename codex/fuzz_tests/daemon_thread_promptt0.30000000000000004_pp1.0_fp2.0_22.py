import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(2)
    print('End daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start non-daemon')
    print('End non-daemon')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
lock = threading.Lock()

def counter(count):
    for i in range(count):
        time.sleep(1)
        with lock:
            print(threading.current_thread().name, i)

def worker(s, e):
    for i in range(s, e):
        time.sleep(1)
        with lock:
            print(threading.current_thread().name, i)

t1 = threading.Thread(name='counter', target=counter, args=(10,
