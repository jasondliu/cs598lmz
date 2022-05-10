import threading
# Test threading daemon

def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)

def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Main thread is still alive
print('Main Thread Exiting')

# Main thread is still alive
# Main Thread Exiting

# Starting: daemon
# Starting: non-daemon
# Exiting : non-daemon
# Exiting : daemon

# Starting: non-daemon
# Exiting : non-daemon
# Main Thread Exiting
# Starting: daemon
# Exiting : daemon


