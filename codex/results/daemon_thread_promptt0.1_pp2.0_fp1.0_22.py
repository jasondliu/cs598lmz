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

def print_square(num):
    lock.acquire()
    try:
        print(num**2)
    finally:
        lock.release()

threads = []
for i in range(10):
    t = threading.Thread(target=print_square, args=(i,))
    threads.append(t)
    t
