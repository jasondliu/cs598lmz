import threading
# Test threading daemon
def daemon():
    print('Starting:')
    time.sleep(2)
    print('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:')
    print('Exiting')

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

def taskofthread(lock):
    for _ in range(100000):
        lock.acquire()
        increment_global()
        lock.release()

def main():
    global x
    x = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=taskofthread, args=(lock,))
    t2 = threading.Thread(target=taskofthread, args=(lock,))

    t1.
