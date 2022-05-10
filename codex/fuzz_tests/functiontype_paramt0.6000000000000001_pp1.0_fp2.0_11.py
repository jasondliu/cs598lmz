from types import FunctionType
list(FunctionType(func.__code__, globals(), func.__name__, func.__defaults__, func.__closure__))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 最后，编写一个既能支持带参数又能支持不带参数的decorator
import functools
def log(text):
    if isinstance(text, FunctionType):
        @functools.wraps(text)
        def decorator(*args, **kw):
            print('call %s():' % text.__name__)
            return text(*args, **kw)
        return decorator
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
