import sys, threading
threading.Thread(target=lambda: sys.stdout.write("thread\n")).start()

print("main\n")
