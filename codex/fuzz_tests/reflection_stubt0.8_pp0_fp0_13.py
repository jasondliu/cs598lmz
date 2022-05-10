fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi
s = fn.__code__

# Reverse iteration should not raise an exception
for c in reversed(s):
    pass

# Testing __sizeof__
import sys
class C:
    def __sizeof__(self):
        return 22
c = C()
size = sys.getsizeof(c)

if size == 22:
    print('PASS')
else:
    print('FAIL', size)
