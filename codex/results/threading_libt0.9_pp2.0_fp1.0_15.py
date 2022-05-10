import threading
threading.stack_size(1024000)

def worker():
    """thread worker function"""
    #print 'Worker'
    return

threads = []
for i in xrange(50000):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
