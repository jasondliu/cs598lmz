import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()
threading.Thread(target=lambda: sys.stdout.write('.')).start()
