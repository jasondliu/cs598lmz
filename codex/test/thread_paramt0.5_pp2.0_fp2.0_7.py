import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from the future\n")).start()
