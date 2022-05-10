import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b\x5b\x33\x3b\x4a')).start()
