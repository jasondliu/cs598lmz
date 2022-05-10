import sys, threading
threading.Thread(target=lambda: sys.stdout.write("running a thread\n")).start()
