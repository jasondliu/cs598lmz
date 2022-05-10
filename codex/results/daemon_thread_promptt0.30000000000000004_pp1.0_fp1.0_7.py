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

# Test threading with queue
def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(threading.current_thread().name, item)
        time.sleep(1)

q = queue.Queue()
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(q,
