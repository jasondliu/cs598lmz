import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read()), daemon=True).start()
