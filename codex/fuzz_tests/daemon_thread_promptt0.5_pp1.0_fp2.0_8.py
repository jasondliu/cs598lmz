import threading
# Test threading daemon
def worker_thread(num):
    """thread worker function"""
    print 'Worker: %s' % num
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker_thread, args=(i,))
    threads.append(t)
    t.start()
    print 'Thread', i, 'started'

print 'Main thread is waiting for the threads to finish'

# Wait for all threads to complete
for t in threads:
    t.join()

print 'All threads have finished'
