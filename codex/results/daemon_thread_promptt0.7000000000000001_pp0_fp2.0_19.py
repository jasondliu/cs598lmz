import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(2)
    print('Stop daemon')

# Test threading non-daemon
def non_daemon():
    print('Start non_daemon')
    print('Stop non_daemon')

# Create daemon thread
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

# Create non-daemon thread
t = threading.Thread(name='non-daemon', target=non_daemon)

# Start daemon thread
d.start()
time.sleep(1)

# Start non-daemon thread
t.start()

# Wait until non-daemon thread finished
t.join()
