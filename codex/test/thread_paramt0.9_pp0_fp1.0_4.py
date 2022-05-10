import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input().swapcase() + ' '),daemon=True).start()
