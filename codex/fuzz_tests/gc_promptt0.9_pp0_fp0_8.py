import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakly referencable object
# that still has finalizers.

import gc, weakref, sys

if (sys.platform.startswith('java') or
    sys.platform == 'cli'):
    # TODO: Jython is not calling __del__, right?
    import warnings
    warnings.warn("This test is not working on the JVM")
    sys.exit(0)

warnings.simplefilter('ignore')

class X(object):
    dead = False
    def f(self):
        sys.stdout.write('.')
        sys.stdout.flush()
    def __del__(self):
        self.dead = True

x = X()
y = X()

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    # Weak references with callbacks
    x_w = weakref.ref(x, x.f)
    y_w = weakref.ref(y, y.f)

    wr = weakref.ref(x)
    del x
    gc.collect
