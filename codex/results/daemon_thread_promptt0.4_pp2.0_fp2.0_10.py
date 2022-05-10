import threading
# Test threading daemon
def daemon():
    print('Start:', threading.current_thread().name)
    time.sleep(2)
    print('End:', threading.current_thread().name)

def non_daemon():
    print('Start:', threading.current_thread().name)
    print('End:', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
