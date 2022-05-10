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

# This will not print anything because the daemon thread is killed before it can print

# The daemon thread is killed when the main thread exits

# The main thread is waiting for the non-daemon thread to exit

# The non-daemon thread is waiting for the daemon thread to exit

# The daemon thread is waiting for the sleep function to return

# The main thread is waiting for the non-daemon thread to exit

# The non-daemon thread is waiting for the daemon thread to exit

# The daemon thread is waiting for the sleep function to return

# The main thread is
