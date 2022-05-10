import threading
# Test threading daemon
def worker():
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
</code>
You should use the <code>thread.daemon</code> property to make the threads quit as soon as the main program exits.
<code>def worker():
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    threads.append(t)
    t.start()
</code>

