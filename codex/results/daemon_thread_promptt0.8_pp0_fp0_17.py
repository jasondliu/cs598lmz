import threading
# Test threading daemon
def daemon():
    p = psutil.Process(os.getpid())
    for x in range(1000000):
        p.cpu_percent()
def non_daemon():
    p = psutil.Process(os.getpid())
    for x in range(1000000):
        p.cpu_percent()
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
n = threading.Thread(name='non-daemon', target=non_daemon)
# Test daemon thread 
start = time.perf_counter()
d.start()
n.start()
d.join()
n.join()
c2 = time.perf_counter()
print(f"{round(c2 - start, 2)} s")

## Set the daemon threads
thread = threading.Thread(target=lambda: None)
# Daemon threads
thread.daemon = True
# Test daemon thread
start = time.perf_counter() 
thread.start()
thread.join()
c1 = time.perf_
