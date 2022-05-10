import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
threading.Thread(target=lambda: sys.stdout.write("world\n")).start()
