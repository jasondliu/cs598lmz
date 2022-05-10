import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x07')).start()

##

import winsound
winsound.Beep(1000, 400)
