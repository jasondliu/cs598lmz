import threading
# Test threading daemon
def daemon():
    print('Start Daemon')
    time.sleep(1)
    print('Stop Daemon')

# Test threading non-daemon
def non_daemon():
    print('Start Non-Daemon')
    print('Stop Non-Daemon')


d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()
