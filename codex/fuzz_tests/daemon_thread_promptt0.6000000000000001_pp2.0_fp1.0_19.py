import threading
# Test threading daemon

def daemon():
    print 'Starting:', threading.currentThread().getName()
    time.sleep(2)
    print 'Exiting :', threading.currentThread().getName()

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print 'Starting:', threading.currentThread().getName()
    print 'Exiting :', threading.currentThread().getName()

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# The main thread exits when all non-daemon threads exit
# The daemon thread exits when the main thread exits

# Output:
# Starting: daemon
# Starting: non-daemon
# Exiting : non-daemon
# Exiting : daemon
 
# If setDaemon(True) is called after start(), a RuntimeError is raised.

# Output:
# Starting: daemon
# Starting: non
