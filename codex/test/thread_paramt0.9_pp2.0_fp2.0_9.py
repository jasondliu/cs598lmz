import sys, threading
threading.Thread(target=lambda: sys.stdout.write('abc\n')).start()
import time
time.sleep(3)

