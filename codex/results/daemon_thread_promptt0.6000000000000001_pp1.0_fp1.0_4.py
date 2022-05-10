import threading
# Test threading daemon mode

def worker():
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    threads.append(t)
    t.start()

print 'Main Thread Exiting'
