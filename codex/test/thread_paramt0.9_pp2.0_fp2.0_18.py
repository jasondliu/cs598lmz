import sys, threading
threading.Thread(target=lambda: sys.stdout.write('multiple threads.\n')).start()
