import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# print('foo')
# print('bar')
# print('quux')
# sys.stdout.write('\n')

import functools
print = functools.partial(print, flush=True)

print('foo')
print('bar')
print('quux')

import time, threading

def foo():
  print('foo')
  time.sleep(0.5)
  print('bar')

threading.Thread(target=foo).start()
time.sleep(0.5)
print('quux')
