import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()

# Python 3.4+
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n'), daemon=True).start()
</code>

