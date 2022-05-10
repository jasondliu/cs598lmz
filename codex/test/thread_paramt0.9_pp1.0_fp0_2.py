import sys, threading
threading.Thread(target=lambda: sys.stderr.write("my stderr\n")).start()
print("my stdout\n")
