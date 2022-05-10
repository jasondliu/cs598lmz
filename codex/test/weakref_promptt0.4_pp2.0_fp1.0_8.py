import weakref
# Test weakref.ref(obj)

import gc
import weakref

class A:
    pass

def callback(r):
    print('callback(', r, ')')

def test():
    a = A()
    r = weakref.ref(a, callback)
    print('a:', a)
    print('r:', r)
    print('r():', r())
    print('deleting a')
    del a
    gc.collect()
    print('r():', r())

test()

# Output:
# a: <__main__.A object at 0x10e8a6f98>
# r: <weakref at 0x10e8b1d68; to 'A' at 0x10e8a6f98>
# r(): <__main__.A object at 0x10e8a6f98>
# deleting a
# callback( <weakref at 0x10e8b1d68; dead> )
# r(): None

# Test weakref.ref(obj, callback)

import gc
