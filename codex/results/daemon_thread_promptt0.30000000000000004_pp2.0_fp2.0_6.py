import threading
# Test threading daemon
import time

# Test threading daemon
def worker():
    print("worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    threads.append(t)
    t.start()

time.sleep(2)
print("main thread")
