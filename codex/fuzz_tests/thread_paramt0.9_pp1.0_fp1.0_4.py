import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
from time import sleep
sleep(4)
</code>
I get no output until the entire program finishes and then "hello" prints. Is it possible to force Python to print the output from the thread?


A:

From the python documentation
<blockquote>
<p>The entire Python program exits when no alive non-daemon threads are
  left.</p>
</blockquote>
So set the target <code>_thread</code> as a daemon:
<blockquote>
<p>This must be set before start() is called, otherwise RuntimeError is raised.</p>
</blockquote>

