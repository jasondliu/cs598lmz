import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello, world!\n')).start()

# Python 2:
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello, world!\n')).start()
