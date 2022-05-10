import sys, threading
threading.Thread(target=lambda: sys.stdout.buffer.write(sys.stdin.buffer.read())).start()
