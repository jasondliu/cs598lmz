import sys, threading
threading.Thread(target=lambda: sys.stdout.write(_thread.contents)).start()
</code>

