gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame
print(gi.gi_code, gi.gi_frame)


class foo(type):
    def __new__(meta, name, bases, dict):
        dict['x'] = dict.get('x') + 1
        cls = type.__new__(meta, name, bases, dict)
        cls.x += 1
        return cls

class A(metaclass=foo, x=3):
    pass

print(A.x)
a = A()
assert a.x == 5

###### Module tests
import sys
print(sys.flags)
sys.stdin.close()
sys.stdin.close() # should work, since close is idempotent

try:
    raise ValueError
except:
    tb = sys.exc_info()[2]
    print(tb.tb_next is None)

import posix
print(posix.stat('foo').st_mode)

import posixpath
print(posixpath.dirname('/usr/local'))

