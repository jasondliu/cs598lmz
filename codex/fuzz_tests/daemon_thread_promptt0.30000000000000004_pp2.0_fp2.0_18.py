import threading
# Test threading daemon

def daemon():
    print('Start daemon')
    time.sleep(5)
    print('Stop daemon')

def non_daemon():
    print('Start non-daemon')
    print('Stop non-daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()
