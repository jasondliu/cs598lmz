import sys, threading
threading.Thread(target=lambda: sys.stdout.write("thread1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread2\n")).start()
