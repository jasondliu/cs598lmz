import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 2\n')).start()
</code>
This prints:
<code>Thread 1
Thread 2
</code>

