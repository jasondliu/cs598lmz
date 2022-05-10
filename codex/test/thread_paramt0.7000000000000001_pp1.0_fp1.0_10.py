import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32m')).start()

