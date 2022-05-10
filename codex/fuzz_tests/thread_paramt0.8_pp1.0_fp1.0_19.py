import sys, threading
threading.Thread(target=lambda: sys.stdout.write("".join(stdout.get_nowait()))).start()
</code>

