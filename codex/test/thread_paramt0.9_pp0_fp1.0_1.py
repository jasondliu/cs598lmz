import sys, threading
threading.Thread(target=lambda: sys.stderr.write("Line\n")).start()
