import sys, threading
threading.Thread(target=lambda: sys.stdout.write("My\nThread\n")).start()
