import sys, threading
threading.Thread(target=lambda: (sys.stdout.write("Hello world\n"), sys.stdout.flush())).start()
</code>

