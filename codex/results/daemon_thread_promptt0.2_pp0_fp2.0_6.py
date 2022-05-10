import threading
# Test threading daemon
import time

def worker():
    print('worker')
    time.sleep(1)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('end')
