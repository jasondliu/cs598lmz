import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\r'+' '*40+'\r')).start()
import sys
