import threading
# Test threading daemon - must be killed to stop
def function():
    print threading.currentThread().getName()
    time.sleep(1)
    print threading.currentThread().getName()
    time.sleep(1)
    print threading.currentThread().getName()
    time.sleep(1)

t = threading.Thread(name='daemon-thread', target=function)
t.setDaemon(True)
t.start()

while True:
    pass

# Test threading event
def function(e):
    print threading.currentThread().getName()
    e.wait()
    print threading.currentThread().getName()

e = threading.Event()
t = threading.Thread(name='non-daemon-thread', target=function, args=(e,))
t.start()

time.sleep(1)
e.set()
