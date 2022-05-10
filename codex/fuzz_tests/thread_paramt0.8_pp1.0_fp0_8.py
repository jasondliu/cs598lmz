import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input("Starting...\n")), daemon=True).start()
</code>
but it is known to have timing problems, doesn't work in some versions of IDLE, and probably only works with stdin anyway.

