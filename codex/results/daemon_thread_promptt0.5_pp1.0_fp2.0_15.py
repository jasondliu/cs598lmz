import threading
# Test threading daemon
def daemon():
    print "I'm running"
    time.sleep(5)
    print "I'm done"

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print "I'm running"
    print "I'm done"

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading.local
class ThreadLocal(threading.local):
    def __init__(self, value=None):
        super(ThreadLocal, self).__init__()
        self.value = value

t = ThreadLocal(10)
print t.value

def f():
    t.value = 20
    print t.value

thread = threading.Thread(target=f)
thread.start()
thread.join()

print t.value

# Test threading.lock
lock = threading.Lock()

def f():
    lock.acquire()
   
