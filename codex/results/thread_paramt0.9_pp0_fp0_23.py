import sys, threading
threading.Thread(target=lambda: sys.stdout.write("sum: " + sum(range(int(input()))) + "\n")).start()
