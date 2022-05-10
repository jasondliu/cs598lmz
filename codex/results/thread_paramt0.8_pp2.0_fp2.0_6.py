import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()
print("Stopped listening to stdin")
