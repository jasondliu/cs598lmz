import sys, threading
threading.Thread(target=lambda:sys.stdout.write("hello")).start()
</code>
In the example above, I'm calling <code>sys.stdout.write</code> in a new thread, so it will run in parallel to the main thread. The main thread will exit, and the child thread will still be running.
The <code>sys.stdout.write</code> call is still happening in the child thread, but I suspect that <code>sys.stdout</code> is being looked up in the main thread.
So I'm wondering, is the <code>sys.stdout</code> in the child thread a reference to the same object as <code>sys.stdout</code> in the main thread?

EDIT:
I'm aware of the following, but I'm more interested in the actual language rules.

Python 3.7: sys.stdout.write() not thread safe?
https://bugs.python.org/issue27301
https://bugs.python.org/issue29298



A:

It's a reference to the same object, yes. From the reference documentation on the <code>sys</code> module
