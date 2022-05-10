import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(1000000))))).start()
</code>
This is a very simple example, but it demonstrates the problem.  The output is not printed to the console until the thread exits.  I would like to see the output as it is generated.
I am using Python 2.7.3 on Windows 7.


A:

The problem is that the output is buffered.  You can fix this by flushing the output after each write:
<code>import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(1000000))))).start()
</code>

