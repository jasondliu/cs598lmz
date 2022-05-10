import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.' * 10000000)).start()
