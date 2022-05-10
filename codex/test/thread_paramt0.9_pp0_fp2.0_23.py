import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread writing\n')).start()
