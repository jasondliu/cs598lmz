import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Printed\n")).start()
threading.Timer(2, lambda: sys.stdout.write("Timeout\n")).start()
