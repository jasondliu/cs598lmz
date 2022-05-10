import threading
# Test threading daemon
def worker_daemon(i):
    print('worker_daemon {}\n'.format(i))

def worker(i):
    print('worker {}\n'.format(i))

threads = []
for i in range(5):
    t = threading.Thread(target=worker_daemon, args=(i,))
    t.setDaemon(True)
    threads.append(t)
    t.start()

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
