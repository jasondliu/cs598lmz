import threading
# Test threading daemon mode
def daemon():
    print('start daemon')
    #t = threading.currentThread()
    #print(t.getName(), 'Starting')
    time.sleep(2)
    #print(t.getName(), 'Exiting')
    print('end daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('start non_daemon')
    t = threading.currentThread()
    print(t.getName(), 'Starting')
    print(t.getName(), 'Exiting')
    print('end non_daemon')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
