import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
</code>
<code>ImportError: No module named class</code>
I've tried changing <code>class</code> to <code>threading</code>, and I've had no success. Can someone point me in the right direction?


A:

I don't know what that exact example is supposed to do, but I assume here that you want to print something and exit immediately afterwards.
I misunderstood your intent initially, and my proposed solution was too complicated, if you just want to do the one thing of printing a line and exiting, you can use this instead as an example:
<code>import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n hello world')).start()
</code>
I see now that you wanted to get out of the program entirely, not just print something.  Here is a solution to do that:
<code>import os
os.execlp('python', 'python', '-c', 'print "Hello world"')
</code>
That causes the "Hello world" to be printed and the
