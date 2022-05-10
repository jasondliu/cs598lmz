import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()
sys.stdout.flush()
</code>

