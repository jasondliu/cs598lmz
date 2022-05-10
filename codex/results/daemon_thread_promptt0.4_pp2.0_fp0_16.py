import threading
# Test threading daemon
def worker():
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()


# Test multiprocessing daemon
def worker():
    print 'Worker'
    return

threads = []
for i in range(5):
    p = multiprocessing.Process(target=worker)
    p.start()
    threads.append(p)

for p in threads:
    p.join()
</code>
The output is:
<code>Worker
Worker
Worker
Worker
Worker
Worker
Worker
Worker
Worker
Worker
</code>
The multiprocessing is much slower than threading, but I need it to be a daemon.
Is there a way to make the multiprocessing daemon?

