import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "In handler"
    print signum
    print frame

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    print "In main loop"
    time.sleep(1)
</code>
The output is:
<code>In main loop
In handler
14
&lt;frame object at 0xb7d5a8c4&gt;
In main loop
In handler
14
&lt;frame object at 0xb7d5a8c4&gt;
In main loop
In handler
14
&lt;frame object at 0xb7d5a8c4&gt;
In main loop
In handler
14
&lt;frame object at 0xb7d5a8c4&gt;
In main loop
In handler
14
&lt;frame object at 0xb7d5a8c4&gt;
In main loop
In handler
14
&lt
