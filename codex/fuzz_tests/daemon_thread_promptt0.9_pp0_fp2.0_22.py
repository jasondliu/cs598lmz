import threading
# Test threading daemonic nature.
# A daemonic thread is destroyed when the main program exits.
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
</code>
Output:
<code>Starting: daemon
Starting: non-daemon
Exiting: non-daemon
</code>

