import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world\n')).start();
</code>
This prints:
<code>Hello world
</code>

