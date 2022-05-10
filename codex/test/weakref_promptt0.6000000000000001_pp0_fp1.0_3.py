import weakref
# Test weakref.ref()
import types

class C(object):
    def __del__(self):
        pass

def f(x):
    return lambda: x

def g(x):
    return weakref.ref(x, f(x))

cases = [f(), f(2), f(2.0), f('x'), f([]), f({}), f(C()), g(C()), f(()),
         f(open(__file__)), f(types)]

if __name__ == '__main__':
    for c in cases:
        try:
            weakref.ref(c)
        except TypeError:
            pass
        else:
            print('unexpected success for', c)
