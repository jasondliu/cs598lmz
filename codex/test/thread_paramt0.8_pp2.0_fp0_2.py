import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(list(map(str,range(1000000))))))\
              .start()

import time
time.sleep(1)

print("Python threading is synchronous")

# Synchronous means that only one thread can be executed at any given time.
# The other thread waits until it's finished.

import threading, sys

threading.Thread(target=lambda: sys.stdout.write('Python '))\
          .start()
threading.Thread(target=lambda: sys.stdout.write('threading '))\
          .start()
threading.Thread(target=lambda: sys.stdout.write('is '))\
          .start()
threading.Thread(target=lambda: sys.stdout.write('synchronous\n'))\
          .start()

print("Python threading is synchronous")

# But as soon as you start working with shared memory, every read and every write have to be locked.
