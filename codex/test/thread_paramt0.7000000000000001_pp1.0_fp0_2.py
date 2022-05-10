import sys, threading
threading.Thread(target=lambda: sys.stdout.write("asd\n")).start()
import time
time.sleep(2)
