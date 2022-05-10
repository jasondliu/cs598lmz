import threading
# Test threading daemon
def daemon():
    print 'Start daemon.'
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        time.sleep(1)
        print 'daemon running...'
    print 'Stop daemon.'

def non_daemon():
    print 'Start non-daemon.'
    time.sleep(2)
    print 'Stop non-daemon.'

# Create daemon thread
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

# Create non-daemon thread
t = threading.Thread(name='non-daemon', target=non_daemon)

# Start threads
d.start()
t.start()

# Wait for daemon thread to exit
d.join()
print 'd.isAlive()', d.isAlive()

# Stop daemon
t.do_run = False

# Wait for non-daemon thread to exit
t.join()
print 't.isAlive()', t.isAlive()

# Print threads
