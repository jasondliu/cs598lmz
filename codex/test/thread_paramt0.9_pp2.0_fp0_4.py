import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 1\n')).start()
