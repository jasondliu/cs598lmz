import sys, threading
threading.Thread(target=lambda: sys.__stdout__.write('D2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('D1\n')).start()
