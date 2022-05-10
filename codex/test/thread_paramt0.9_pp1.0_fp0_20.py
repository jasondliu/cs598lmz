import sys, threading
threading.Thread(target=lambda: sys.stdout.write("blah\n")).start()
