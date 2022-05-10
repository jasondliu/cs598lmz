import sys, threading
threading.Thread(target=lambda: sys.stderr.write('Hello world\n')).start()
