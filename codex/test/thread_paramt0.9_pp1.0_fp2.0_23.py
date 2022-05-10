import sys, threading
threading.Thread(target=lambda: sys.stdin.readlines()).start()
