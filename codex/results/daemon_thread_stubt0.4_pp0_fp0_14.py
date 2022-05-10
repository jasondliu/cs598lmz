import sys, threading

def run():
    while True:
        print("thread 1")
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print("thread 2")
    sys.stdout.flush()
    time.sleep(1)
</code>
I can see that both threads are running, but they are not running in parallel.
I am using Python 3.5.2


A:

<code>print</code> is not thread-safe.  You can't just call it from multiple threads without synchronizing it.  For example, you could use a <code>threading.Lock</code>.  Or, you could use <code>sys.stdout.write</code> instead of <code>print</code>, since it doesn't acquire a lock.

