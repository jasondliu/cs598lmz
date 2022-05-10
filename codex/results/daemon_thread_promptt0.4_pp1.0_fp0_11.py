import threading
# Test threading daemon
# https://docs.python.org/2/library/threading.html#threading.Thread.daemon

def worker():
    """thread worker function"""
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
