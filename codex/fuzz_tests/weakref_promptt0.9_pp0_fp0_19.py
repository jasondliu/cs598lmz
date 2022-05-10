import weakref
# Test weakref.ref(myobj).proxy == myobj

import weakref

class Ref:
    def __init__(self, obj):
        self.r = weakref.ref(obj)

class C:
    def __init__(self, x=0):
        self.x = x
    def bump(self):
        self.x += 1

def main():
    c1 = C(1)
    r = Ref(c1)
    x = r.r.proxy      # The next line may fail with x != c1.
    assert x.x == c1.x
    c1.bump();         # This may invalidate the weakref, in which case the
    assert x.x == c1.x    # next line would trigger an attr lookup error.

main()
main()

del main
del Ref
del C
import gc
for i in range(300):
    gc.collect()
