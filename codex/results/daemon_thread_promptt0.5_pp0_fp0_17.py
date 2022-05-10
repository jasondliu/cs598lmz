import threading
# Test threading daemon

def daemon():
    print('Start daemon')
    time.sleep(1)
    print('Stop daemon')

def non_daemon():
    print('Start non-daemon')
    time.sleep(1)
    print('Stop non-daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print('End')

# Output:
# Start daemon
# Start non-daemon
# Stop non-daemon
# End
# Stop daemon

# It's clear that the daemon thread is terminated immediately when the main thread is terminated.
