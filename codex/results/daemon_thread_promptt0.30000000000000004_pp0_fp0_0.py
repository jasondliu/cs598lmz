import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(2)
    print('Exit daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start non-daemon')
    print('Exit non-daemon')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading lock
lock = threading.Lock()

def thread_lock(i):
    print('Thread {}: starting'.format(i))
    lock.acquire()
    print('Thread {}: has lock'.format(i))
    time.sleep(2)
    print('Thread {}: releasing lock'.format(i))
    lock.release()
    print('Thread {}: finished'.format(i))

for i in range(5):
    t = threading.Thread(target=thread_lock, args=(i,))
    t.start()

# Test threading
