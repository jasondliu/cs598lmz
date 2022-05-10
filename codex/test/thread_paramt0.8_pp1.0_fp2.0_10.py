import sys, threading
threading.Thread(target=lambda: sys.stdout.write("%s\n" % "hello")).start()
