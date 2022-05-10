import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hey!\n')).start()
