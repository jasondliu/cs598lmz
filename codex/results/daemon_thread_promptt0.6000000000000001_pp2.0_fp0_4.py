import threading
# Test threading daemonic

def worker():
    """thread worker function"""
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    threads.append(t)
    t.start()

print 'Exiting Main Thread'
</code>

