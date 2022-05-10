import sys, threading

def run():
    while True:
        sys.stdout.write('X')
        sys.stdout.flush()

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

while True:
    print "O"
</code>
Save it as <code>test.py</code>. Now, run it:
<code>$ ./test.py &gt; /dev/null
</code>
Both threads are running at the same time.

