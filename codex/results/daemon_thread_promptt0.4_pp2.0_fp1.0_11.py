import threading
# Test threading daemon

def worker():
    print "Worker"
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    threads.append(t)
    t.start()

print "Main thread"
