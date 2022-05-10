import threading
# Test threading daemon
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting:', threading.current_thread().name)
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting:', threading.current_thread().name)
t = threading.Thread(name='non-daemon', target=non_daemon)
d.start()
t.start()
d.join()
t.join()

# Test threading pool
def worker(num):
    """thread worker function"""
    print('Worker:', num)
    return
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Test threading lock
def worker(num):
    """thread worker function"""
    print('
