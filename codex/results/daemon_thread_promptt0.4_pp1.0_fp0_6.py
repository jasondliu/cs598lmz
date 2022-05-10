import threading
# Test threading daemon

def worker(num):
    print('Worker: %s' % num)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

print('threads: %s' % threads)

# Set daemon
for t in threads:
    t.setDaemon(True)

print('threads: %s' % threads)

# Check daemon
for t in threads:
    print('is daemon: %s' % t.isDaemon())

# Join
for t in threads:
    t.join()

print('Exiting main thread')
