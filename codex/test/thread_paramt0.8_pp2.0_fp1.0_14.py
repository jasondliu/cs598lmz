import sys, threading
threading.Thread(target=lambda: sys.stdout.write('hoi\n')).start()
