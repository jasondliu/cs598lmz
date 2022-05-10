import threading
# Test threading daemon

def daemon():
    print('Daemon thread started')
    time.sleep(2)
    print('Daemon thread finished')

def non_daemon():
    print('Non daemon thread started')
    print('Non daemon thread finished')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
t = threading.Thread(name='non_daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print('Main thread finished')

# Daemon thread started
# Non daemon thread started
# Non daemon thread finished
# Main thread finished
# Daemon thread finished
 
# Main thread finished before daemon thread finished

# Daemon thread started
# Non daemon thread started
# Non daemon thread finished
# Main thread finished
# Daemon thread finished

# Main thread finished before daemon thread finished

# Daemon thread started
# Non daemon thread started
# Non daemon thread finished
# Daemon thread finished
# Main thread finished

# Main thread finished before daemon
