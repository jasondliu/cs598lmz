from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_varnames)

# ['x']

# getattr(obj, 'attribute', default)

# getattr(x, 'foobar')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'foobar'

# getattr(x, 'foobar', 'default')
# 'default'

# from types import MethodType
# def f(self, x, y):
#     return min(x, x+y)
# class C:
#     pass
# obj = C()
# obj.method = MethodType(f, obj)
# obj.method(1, 2)

# 1

# obj.method('spam', 'eggs')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in f
# TypeError: '<' not supported between instances of 'str' and
