fn = lambda: None
# Test fn.__code__.co_argcount
# fn.__code__.co_argcount += 1
# test fn(*(1, 2, 3, 4, 5))

# # 3.1.7.1.1. fn.__doc__
# fn = lambda: None
# print(fn.__doc__)
# fn.__doc__ = 'Hello'
# print(fn.__doc__)

# # 3.1.7.1.2. fn.__globals__
# fn = lambda: None
# print(fn.__globals__)
# fn.__globals__['g'] = 1
# print(fn.__globals__)
# # test fn()

# # 3.1.7.1.3. fn.__name__
# fn = lambda: None
# print(fn.__name__)
# fn.__name__ = 'hello'
# print(fn.__name__)
# # test fn()

# 3.1.7.2. fn.__closure__
# fn = lambda: x
# print(fn
