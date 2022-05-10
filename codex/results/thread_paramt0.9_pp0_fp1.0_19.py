import sys, threading
threading.Thread(target=lambda: sys.__stdout__.flush()).start()

# Your code goes here

sys.stdout.write('y')
sys.stdout.flush() # don't forget to flush!

print('hello')
print('hello', file=sys.__stdout__)
print('goodbye', file=sys.__stderr__)

import signal # signal.pause
signal.pause()
