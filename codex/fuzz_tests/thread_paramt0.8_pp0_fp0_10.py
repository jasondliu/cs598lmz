import sys, threading
threading.Thread(target=lambda: sys.stdout.write('my stdout\n')).start()
threading.Thread(target=lambda: sys.stderr.write('my stderr\n')).start()
</code>

