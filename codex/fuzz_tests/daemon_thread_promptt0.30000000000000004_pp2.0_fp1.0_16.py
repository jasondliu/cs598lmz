import threading
# Test threading daemon

def daemon():
    print('Starting:', threading.currentThread().getName())
    time.sleep(2)
    print('Exiting :', threading.currentThread().getName())

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:', threading.currentThread().getName())
    print('Exiting :', threading.currentThread().getName())

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# The daemon thread is killed before it can complete.

# The output is:
# Starting: daemon
# Starting: non-daemon
# Exiting : non-daemon
# Exiting : daemon

# If you comment out the d.setDaemon(True) line, the output looks like this:
# Starting: daemon
# Starting: non-daemon
# Exiting : non-daemon
#
