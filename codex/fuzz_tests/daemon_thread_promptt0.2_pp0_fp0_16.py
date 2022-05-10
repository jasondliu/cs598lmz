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
x = 0

def increment_global():
    global x
    x += 1

def taskofThread(lock):
    for _ in range(100000):
        lock.acquire()
        increment_global()
        lock.release()

def main_task():
    global x
    x = 0

    lock = threading.Lock()

    t1 = threading
