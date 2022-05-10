import sys, threading
threading.Thread(target=lambda: sys.stdout.write("asd\n")).start()
import time
time.sleep(2)
</code>
Unfortunately, it seems that the output of the thread is being buffered and the thread terminates before it can get it printed.
Is there a way to disable buffering and force the output to be printed as soon as it's available?
(I know I can use something like <code>threading.Thread(target=lambda: sys.stdout.write("asd\n"); sys.stdout.flush()).start()</code>, but I'm looking for a non-intrusive way to disable the buffering, so that I don't have to call <code>flush</code> explicitly whenever I have a thread that prints something)


A:

You can set the file to line buffering:
<code>sys.stdout = open(sys.stdout.fileno(), 'w', 1)
</code>
It will automatically flush whenever a newline is printed.

