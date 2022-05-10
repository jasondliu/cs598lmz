import threading
# Test threading daemon

def daemon():
    print('Start daemon')
    time.sleep(2)
    print('End daemon')

def non_daemon():
    print('Start non daemon')
    print('End non daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print('End of main thread')

# Start daemon
# Start non daemon
# End non daemon
# End of main thread
# End daemon

# d.join() will wait until d thread is finished
# d.setDaemon(True) will cause the thread to exit when the main thread
# exits.

# If you comment out both d.join() and d.setDaemon(True)

# Start daemon
# Start non daemon
# End non daemon
# End of main thread

# You'll see that the daemon thread never finishes because the main thread
#
