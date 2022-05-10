import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 3\n')).start()

# Hello from thread 1
# Hello from thread 2
# Hello from thread 3

# Threads can also be used to offload work to background threads,
# allowing the main thread to continue running in the meantime.
# For example, the following code runs a function in the background
# while the main thread continues to run:

import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

# T-minus 10
# T-minus 9
# T-minus 8
# T-minus 7
# T-minus 6
# T-minus 5
# T-minus 4

