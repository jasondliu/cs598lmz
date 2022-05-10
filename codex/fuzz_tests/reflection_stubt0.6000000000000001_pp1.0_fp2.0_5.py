fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    fn()
except TypeError:
    print('TypeError')


# __cached__
# __class__
# __closure__
# __code__
# __defaults__
# __dict__
# __doc__
# __get__
# __globals__
# __kwdefaults__
# __name__
# __qualname__
