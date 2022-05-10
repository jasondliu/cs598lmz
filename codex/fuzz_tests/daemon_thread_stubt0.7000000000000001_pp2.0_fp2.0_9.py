import sys, threading

def run():
    print "In run"
    sys.exit(0)

thread = threading.Thread(target=run)
thread.start()
print "Started"
thread.join()
print "Joined"
</code>
The output is:
<code>Started
Joined
In run
</code>
I would have expected <code>sys.exit(0)</code> to terminate the main thread as well as the thread that it was executed in.
Is this the correct behavior?  Is <code>sys.exit</code> supposed to terminate the main thread?


A:

<code>sys.exit</code> is not intended to terminate the main thread as well as the thread that it was executed in.
See the documentation for <code>thread.exit</code>:
<blockquote>
<p>When the main thread exits, it is system defined whether the other threads survive. On SGI IRIX using the native thread implementation, they are killed without executing try ... finally clauses or executing object destructors. On Mac OS X it appears all threads are killed when the main thread exits.</p>
</blockquote>

