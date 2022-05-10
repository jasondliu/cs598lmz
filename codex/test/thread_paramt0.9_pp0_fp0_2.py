import sys, threading
threading.Thread(target=lambda: sys.stdin.isatty()).start()
sys.exit()
