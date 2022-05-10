import threading
# Test threading daemon

def worker(num):
    print("Worker: %d" % num)

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
