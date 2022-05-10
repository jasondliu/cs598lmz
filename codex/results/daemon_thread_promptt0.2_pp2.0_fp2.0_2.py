import threading
# Test threading daemon
import time

def worker():
    print("worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Threads finished")

# Test threading daemon
def daemon():
    print("daemon")
    time.sleep(1)
    print("daemon")

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print("non-daemon")

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()
