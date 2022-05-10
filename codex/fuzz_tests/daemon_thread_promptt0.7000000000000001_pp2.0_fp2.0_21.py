import threading
# Test threading daemon
def worker(id):
    print "I'm worker %d" % id
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

# Test threading.timer
from threading import Timer
def hello():
    print "hello, world"

t = Timer(5.0, hello)
t.start() # after 30 seconds, "hello, world" will be printed

# Test threading.local
from threading import local
class A:
    x = 0
    def __init__(self):
        self.x = 0

mydata = local()
mydata.x = 0

def f():
    mydata.x = mydata.x + 1
    print mydata.x

t1 = threading.Thread(target=f)
t2 = threading.Thread(target=f)
t3 = threading.Thread(target=f)
