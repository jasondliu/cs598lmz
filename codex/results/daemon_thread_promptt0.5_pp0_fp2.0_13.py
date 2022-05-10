import threading
# Test threading daemon
def daemon():
    print('Start')
    time.sleep(2)
    print('Exit')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start')
    print('Exit')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()
