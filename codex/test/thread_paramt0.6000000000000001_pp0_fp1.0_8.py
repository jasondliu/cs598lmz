import sys, threading
threading.Thread(target=lambda: sys.stderr.write("hello world\n")).start()
