import sys, threading
threading.Thread(target=lambda: sys.stdout.write("E\n")).start()
threading.Thread(target=lambda: sys.stdout.write("F\n")).start()
sys.stdout.write("A\n")
sys.stdout.write("B\n")
sys.stdout.write("C\n")
sys.stdout.write("D\n")
