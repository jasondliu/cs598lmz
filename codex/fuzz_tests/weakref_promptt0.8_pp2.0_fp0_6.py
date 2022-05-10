import weakref
# Test weakref.ref() with an old-style class instance.

import weakref


class Foo:

    def f(self):
        pass


f = Foo()
r = weakref.ref(f)

print(r())
f.f()
