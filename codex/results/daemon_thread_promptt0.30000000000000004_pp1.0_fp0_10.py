import threading
# Test threading daemon

def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting:', threading.current_thread().name)

def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting:', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# If a daemon thread creates another daemon thread, the new thread is also a daemon.
# If a non-daemon thread creates a daemon thread, the new thread is also a non-daemon.

# If the main thread is non-daemon, it waits for all non-daemon threads to exit before exiting.
# If the main thread is daemon, it exits when all non-daemon threads are finished.

#
