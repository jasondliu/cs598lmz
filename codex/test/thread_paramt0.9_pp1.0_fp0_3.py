import sys, threading
threading.Thread(target=lambda: sys.exit(1)).start()
print("This line should appear before the exit of the thread.")
