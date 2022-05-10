import ctypes

class S(ctypes.Structure):
    x = ctypes.c_wchar
    def func(self): return 1
    def __str__(self): return 'in S'


class FOO(object):
    _x = None
    @property
    def x(self):
        if self._x is None:
            self._x = S()
        return self._x

    def __str__(self): return 'in foo'
    def __repr__(self): return "FOO()"
</code>

>>> foo = FOO()
>>> foo.x
in S
>>> foo.x.x
in S
>>> foo.x.x.func()
1

In other words, why do you get a new object every time there's a dot, and finally seeing <code>&lt;__main__.S object at 0x000000000645D908&gt;</code>?


A:

The best way that I can explain it is with a different example, hopefully this will help you understand what is going on in your code. I'm going to use a different structure, but it will have the same issue as yours.

