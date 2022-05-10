import threading
# Test threading daemon
def daemon():
    print('Daemon starting')
    time.sleep(2)
    print('Daemon Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Non-daemon starting')
    print('Non-daemon Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
