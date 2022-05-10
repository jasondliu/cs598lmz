import sys, threading
threading.Thread(target=lambda: sys.stdout.write("a\n")).start()
print("Hello World")
