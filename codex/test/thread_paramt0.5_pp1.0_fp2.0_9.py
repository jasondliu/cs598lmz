import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello World\n")).start()

# In Python 3.4 and up, it's even simpler:
from threading import Thread
Thread(target=lambda: print("Hello World")).start()
