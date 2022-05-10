import types
types.ClassType
bc0 = file('baseclass.py')
bc = imp.load_module('baseclass', bc0, 'baseClass.py', ('.py', 'U', 1))

c0 = file('class2.py')
c = imp.load_module('class2', c0, 'class2.py', ('.py', 'U', 1))

c.C = type('C', (c.B, bc.A), {})


class C(c.B):
    pass

assert isinstance(C(), bc.A)
assert issubclass(C, bc.A)

assert isinstance(C(), c.B)
assert issubclass(C, c.B)
