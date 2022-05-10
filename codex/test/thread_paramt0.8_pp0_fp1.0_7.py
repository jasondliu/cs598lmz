import sys, threading
threading.Thread(target=lambda: sys.stdout.read(1)).start()   # Don't let the readline block return before the client is calling
