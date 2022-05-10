import types
types.MethodType(lambda self, x: x + 1, None)

# types.MethodType(lambda self, x: x + 1, None)
# <bound method <lambda> of <class 'NoneType'>>
# >>> types.MethodType(lambda self, x: x + 1, None)(2)
# 3

# >>> class C:
# ...     pass
# ...
# >>> def f(self, x):
# ...     return min(x, self.default)
# ...
# >>> C.f = f
# >>> C.default = 10
# >>> C().f(3)
# 3
# >>> C.default = 3
# >>> C().f(3)
# 3
# >>> C.default = 2
# >>> C().f(3)
# 2

# >>> class C:
# ...     def f(self, x):
# ...         return min(x, self.default)
# ...     default = 10
# ...
# >>> C.default = 3
# >>> C().f(3)
# 3
# >>> C.default = 2
# >>> C
