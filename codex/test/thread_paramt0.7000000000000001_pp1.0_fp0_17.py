import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world\n")).start()

# Python 2.x
import thread
