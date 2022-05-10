from types import FunctionType
list(FunctionType(lambda: None, {}, '', (), None).__dict__.keys())
# ['__code__', '__name__', '__doc__', '__dict__', '__module__', '__defaults__', '__kwdefaults__', '__annotations__', '__globals__', '__closure__', '__qualname__']

# 5.3.3.1
# not all functions are callable.
# to define a function that only retrieves attributes,
# use the function new_style(func, **attrs) below
class new_style:
    def __init__(self, func, **attrs):
        self.func = func
        self.attrs = attrs
    def __getattr__(self, attr):
        return self.attrs[attr]
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

# 5.3.3.3
# the function below shows how to define a function that
# returns None when passed a single argument, or the
# argument itself
