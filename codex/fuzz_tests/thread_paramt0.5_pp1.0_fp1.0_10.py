import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

while 1:
    pass
