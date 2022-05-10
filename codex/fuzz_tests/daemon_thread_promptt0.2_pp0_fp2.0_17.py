import threading
# Test threading daemon

def daemon():
    print('Starting:')
    time.sleep(2)
    print('Exiting')

def non_daemon():
    print('Starting:')
    print('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Output:
# Starting:
# Starting:
# Exiting
# Exiting

# The daemon thread d is killed when the main thread exits.
# The non-daemon thread t is still running after the main thread exits.

# The daemon threads are terminated automatically when the main thread exits.
# The non-daemon threads are not terminated automatically.
# The main thread waits for the non-daemon threads to complete before exiting.

# The daemon threads are used for background activities.
# The non-daemon threads are used for foreground activities.

# The daemon threads are not
