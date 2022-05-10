import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32mHello World\x1b[0m\n')).star
