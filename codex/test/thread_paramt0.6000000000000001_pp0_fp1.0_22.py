import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input('Line 1: ')), daemon=True).start()
threading.Thread(target=lambda: sys.stdout.write(input('Line 2: ')), daemon=True).start()
