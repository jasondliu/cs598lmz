import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello\n")).start()

import time
time.sleep(1)
