import sys, threading
threading.Thread(target=lambda: sys.stderr.write("you're in for some fun.")).start()
