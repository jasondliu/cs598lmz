import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(10)))))
</code>
But it doesn't work.
I'm using Python 3.6.8.
How can I print the output without waiting for the process to finish?


A:

You can try this:
<code>import sys, threading
threading.Thread(target=lambda: print('\n'.join(map(str, range(10)))))
</code>

