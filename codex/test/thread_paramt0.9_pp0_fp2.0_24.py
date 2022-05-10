import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
threading.Timer(5.0/10.0, lambda: sys.stderr.write('\n')).start()
