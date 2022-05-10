import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread\n'), name="test1").start()

