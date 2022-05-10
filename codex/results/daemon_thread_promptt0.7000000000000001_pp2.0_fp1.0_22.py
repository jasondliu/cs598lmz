import threading
# Test threading daemon attribute

daemon = threading.currentThread().isDaemon()
print('Daemon status:', daemon)

# Daemon status: False
# The main thread is not a daemon thread

daemon = threading.current_thread().isDaemon()
print('Daemon status:', daemon)

# Daemon status: False

# start a new thread
t = threading.Thread(target=print, args=('Bazinga',))
t.isDaemon()

# False

t.setDaemon(True)
t.isDaemon()

# True

t.start()
t.join()

# Bazinga

t = threading.Thread(target=print, args=('Carry on',))
t.daemon = True
t.start()
t.join()

# Carry on
