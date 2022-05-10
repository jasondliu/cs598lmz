import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()

# Python 3.4
from threading import Thread
Thread(target=lambda: sys.stdout.write('Hello World\n')).start()
