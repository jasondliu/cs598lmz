import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello World\n")).start()

# Python 2.x
import threading
threading.Thread(target=lambda: sys.stdout.write("Hello World\n")).start()
