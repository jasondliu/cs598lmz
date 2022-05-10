import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
from time import sleep
sleep(4)
