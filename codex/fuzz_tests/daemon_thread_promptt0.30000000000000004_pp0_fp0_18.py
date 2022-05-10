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

# Test threading lock
lock = threading.Lock()

def do_this_with_lock(i):
    lock.acquire()
    try:
        print('{}'.format(i))
    finally:
        lock.release()

def do_this_without_lock(i):
    print('{}'.format(i))

def run_threads(func):
    threads = []
    for i in range(5):
        t = threading.Thread(target=func, args=(i,))
        threads.append(t)
        t.start()
    for t in threads
