import types
types.SimpleNamespace

from inspect import getargspec

# tmp = {
#     'x': None
# }
#
#
# def foo(x):
#     print(tmp['x'])
#
#
# def proxy(*args, **kwargs):  # x
#     tmp['x'] = args[0]
#     return foo
#
#
# proxy1 = proxy(None)

# print(args, kwargs)
# print(foo.__kwdefaults__)
# x, y,
# x => [args[0]] + list(kwargs.values()) => [None] + [] => [None]
# print(list(kwargs.values()))
# x = args[0]

# proxy.__kwdefaults__ = {}

# print(getargspec(foo))
# print(getargspec(proxy))

# print(*[x for x in foo.__code__.co_varnames if x != 'args' and x != 'kwargs'])
# print(*[x for x in proxy.__code__.
