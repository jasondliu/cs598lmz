import threading
# Test threading daemon mode

def worker():
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    threads.append(t)
    t.start()

print 'Main thread waiting'
main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    t.join()
print 'Main thread exit'
