import threading
# Test threading daemon
def daemon():
    print('Start')
    time.sleep(5)
    print('Exit')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
d.start()
d.join()

# Test threading non-daemon
def non_daemon():
    print('Start')
    time.sleep(5)
    print('Exit')

t = threading.Thread(name='non-daemon', target=non_daemon)
t.start()
t.join()
