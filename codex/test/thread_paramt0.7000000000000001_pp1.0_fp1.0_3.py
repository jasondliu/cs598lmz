import sys, threading
threading.Thread(target=lambda: sys.stdout.write("B")).start()
threading.Thread(target=lambda: sys.stdout.write("C")).start()
print("A")
