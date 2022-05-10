import threading
# Test threading daemon
def daemon(a, b):
    c = a + b
    print c
d = threading.Thread(target=daemon, args=(1, 2))
d.daemon = True
d.start()
# make a new threading
import threading
def daemon():
    print 'Hello World!'
t = threading.Thread(target=daemon)
# make it a daemon
t.daemon = True
# start it
t.start()
# test if it is alive
t.is_alive()
# Make threading with 2 arguments
import threading
def daemon(a, b):
    c = a + b
    print c
t = threading.Thread(target=daemon, args=(1, 2, ))
t.daemon = True
t.start()
# Test threading lock
import threading
class Counter(object):
    def __init__(self):
        self.val = 0
        self.lock = threading.Lock()
    def inc(self):
        with self.lock:
            self.val += 1
    def dec(self):
