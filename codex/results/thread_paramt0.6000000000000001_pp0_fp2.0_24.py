import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(1, 10001))))).start()
</code>
The idea is that we have a <code>Thread</code> that prints out all the numbers from 1 to 10000.
However, the printing is not done in the main thread, but in a separate thread.
This means that the main thread can continue execution, and it doesn't have to wait for the printing thread to finish.
This is why the output is not in order.

