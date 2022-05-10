import threading
# Test threading daemon

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

d = threading.Thread(name='daemon', target=worker)
d.setDaemon(True)

t1 = threading.Thread(name='t1', target=worker)
t2 = threading.Thread(target=worker) # use default name

d.start()
t1.start()
t2.start()

d.join()

print('Exiting main!')

# The main thread is not waiting for the daemon thread to complete
# in this case, because the daemon thread is running in the background
# However, the daemon thread is not allowed to block the program from exiting
# and it's terminated when the main thread is done.

# Output
# daemon Starting
# daemon Exiting
# t1 Starting
# Thread-1 Starting
# Exiting main!

# If you run this script without the -daemon argument, the output will be
# different:


