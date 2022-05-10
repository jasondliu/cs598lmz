import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x07')).start()
