import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print(gc.garbage)
import os

class File:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'File({!r})'.format(self.name)

    def __del__(self):
        print('removing {}'.format(self.name))
        try:
            os.remove(self.name)
            print('removed {}'.format(self.name))
        except FileNotFoundError:
            pass

f1 = File('foo')
f2 = f1
f3 = f1

#del f1
#del f2
del f3

import weakref
s1 = {1, 2, 3}
s2 = s1

def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)


