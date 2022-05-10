import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()
</code>
I expected the output to be interleaved:
<code>Hello from thread 1
Hello from thread 2
</code>
But what I got was:
<code>Hello from thread 1
Hello from thread 2
</code>
I also tried <code>sys.stderr</code> instead of <code>sys.stdout</code> and got the same behavior. I'm running Python 2.6.2 on Mac OS X 10.6.4.
I tried to find anything related to this on Google, but the first results were how to interleave output from multiple threads (which I already figured out).


A:

stdout and stderr are actually line buffered by default in Python, so the <code>write</code> calls don't produce any output until a newline is printed.  You can see this by calling <code>sys.stdout.flush()</code> after each <code>write</
