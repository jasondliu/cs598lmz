import sys, threading
threading.Thread(target=lambda: sys.stdout.write("In thread\n")).start()
