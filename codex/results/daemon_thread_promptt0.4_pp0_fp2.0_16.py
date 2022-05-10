import threading
# Test threading daemon

def worker():
    print "Worker"
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    threads.append(t)
    t.start()

print "Exiting"
</code>
This code runs, but the threads don't print anything.  I would expect to see 5 "Worker" lines printed.  If I remove the setDaemon line, it works as I would expect.  I've read the documentation, and it seems like I'm doing this right.  Am I missing something?


A:

I think the issue is that the main thread is exiting before the worker threads have a chance to print anything.  Try this:
<code>import threading
# Test threading daemon

def worker():
    print "Worker"
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    threads.append(t)
    t.start()

