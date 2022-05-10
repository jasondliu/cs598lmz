import sys, threading
threading.Thread(target=lambda: threading.local().foo).start()
