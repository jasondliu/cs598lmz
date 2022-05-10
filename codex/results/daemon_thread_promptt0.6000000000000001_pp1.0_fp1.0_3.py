import threading
# Test threading daemon
def worker(num):
    print('Worker: %s' % num)
    return
# Create thread
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
# Start thread
for thread in threads:
    thread.start()
# Is the main thread waiting for thread to complete?
for thread in threads:
    thread.join()
print('Done')

# Daemon
# A daemon thread will shut down immediately when the program exits.
# To create a daemon thread, set the daemon property to True when creating the thread.
def daemon():
    print('Starting:')
    time.sleep(2)
    print('Exiting')
# Create thread
d = threading.Thread(name='daemon', target=daemon)
# Set daemon to true
d.setDaemon(True)
# Start thread
d.start()
# Is the main thread waiting for thread to complete?
d.join()
print('Done')

# Subclass
# Create a subclass of the Thread class
