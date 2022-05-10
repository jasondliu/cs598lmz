import sys, threading
threading.Thread(target=lambda: sys.stdout.write('abc'), daemon=True).start()
