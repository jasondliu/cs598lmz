import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()
