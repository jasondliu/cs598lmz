import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 2\n")).start()

print("Hello from main thread")

## Hello from main thread
## Hello from thread 2
