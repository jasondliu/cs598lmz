import threading
threading.Event().set()
def hello(name):
    """wait for the event to be set before doing anything"""
    print 'hello', name
    event.wait()
    # after the event is set, wait a random amount of time
    # to simulate real work
    time.sleep(random.random())
    print 'goodbye', name

threads = []
for i in range(5):
    t = threading.Thread(target=hello, args=(i,))
    threads.append(t)
    t.start()

# ... do some other stuff ...

# when you want the threads to proceed
event.set()
# or, to just kill them:
# event.set()
# event.clear()
</code>

