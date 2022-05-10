import sys, threading
threading.Thread(target=lambda: sys.stdout.write(unicode('do the thing!\n', 'utf-8'))).start()
