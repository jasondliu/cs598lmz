import threading
# Test threading daemon
# https://stackoverflow.com/questions/190010/daemon-threads-explanation

def daemon():
    print 'Starting:', threading.currentThread().getName()
    time.sleep(2)
    print 'Exiting :', threading.currentThread().getName()

def non_daemon():
    print 'Starting:', threading.currentThread().getName()
    print 'Exiting :', threading.currentThread().getName()

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# d.join()
t.join()

# d.join()

print 'Exiting Main Thread'

# Starting: non-daemon
# Starting: daemon
# Exiting : non-daemon
# Exiting Main Thread
# Exiting : daemon
# Exiting Main Thread

# Starting: non-daemon
# Starting:
