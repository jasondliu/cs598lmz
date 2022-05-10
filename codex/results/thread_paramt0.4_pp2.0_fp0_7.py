import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32mHello \x1b[1;34mWorld\x1b[0m\n')).start()

import time
time.sleep(0.01)

print('\x1b[1;32mHello \x1b[1;34mWorld\x1b[0m')
print('\x1b[1;32mHello \x1b[1;34mWorld\x1b[0m')
print('\x1b[1;32mHello \x1b[1;34mWorld\x1b[0m')
print('\x1b[1;32mHello \x1b[1;34mWorld\x1b[0m')
print('\x1b[1;32mHello \x1b[1;34mWorld\x1b[0m')
print('\x1b[1;32mHello \x1b[1;34mWorld\x1b[0m')
print('\x1b[1;32mHello \x
