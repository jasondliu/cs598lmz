import threading
# Test threading daemon

def worker():
    print "Worker"
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    threads.append(t)
    t.start()

print "Exiting Main Thread"
</code>
This code will exit without printing "Worker" 5 times.
If I change <code>t.daemon = True</code> to <code>t.daemon = False</code>, then it will print "Worker" 5 times before exiting.
Why is this?


A:

<code>daemon</code> threads are killed when the main thread exits.
From the docs:
<blockquote>
<p>A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property.</p>
</blockquote>

