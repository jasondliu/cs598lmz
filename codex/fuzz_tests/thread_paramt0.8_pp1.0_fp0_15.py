import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world".upper())).start()
</code>
The thread never appears to start. Unfortunately, I can't use the <code>gevent</code> library for this.


A:

You have a threading deadlock; <code>sys.stdout</code> is  a Python wrapper around the C stdout, and it uses Python code to implement printing. When that happens, it grabs the global interpreter lock (GIL). The <code>threading</code> module uses the GIL to implement safe thread switching, and in particular, it grabs the GIL before it switches threads. Thus, your thread cannot be scheduled since it currently holds the GIL.
The following code, however, works fine:
<code>import sys, threading, random
def puts(s):
    sys.stdout.write(s + '\n')
threading.Thread(target=lambda: puts("hello world".upper())).start()
random.seed(1)
while threading.active_count() &gt; 1:
    time.sleep(random.normalvariate(0.1, 0.05
