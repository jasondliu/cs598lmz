import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# Python 3
from threading import Thread
Thread(target=lambda: print(input())).start()

# Python 3
from threading import Thread
Thread(target=lambda: sys.stdout.write(input())).start()
