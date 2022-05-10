import threading
# Test threading daemon
def worker():
    # print threading.currentThread().getName(), 'Starting'
    while True:
        time.sleep(0.1)
        # print threading.currentThread().getName(), 'Exiting'

d = threading.Thread(name='daemon', target=worker)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=worker)

d.start()
t.start()

d.join()
t.join()
