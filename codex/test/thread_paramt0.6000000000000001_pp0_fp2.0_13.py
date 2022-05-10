import sys, threading
threading.Thread(target=lambda: sys.stdout.write('a')).start()
threading.Thread(target=lambda: sys.stdout.write('b')).start()
