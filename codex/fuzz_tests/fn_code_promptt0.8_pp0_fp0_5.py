fn = lambda: None
# Test fn.__code__ if available, or else test fn.func_code
has_code_attrs = (hasattr(fn, '__code__') or hasattr(fn, 'func_code'))
has_closure_attrs = (has_code_attrs and hasattr(fn, '__closure__') or hasattr(fn, 'func_closure'))
if has_closure_attrs:
    def has_args(func):
        args = (getattr(func, '__code__', getattr(func, 'func_code', 1))).co_argcount
        return args != 0
else:
    def has_args(func):
        args = func.__code__.co_argcount
        return args != 0

# Wraps a method to provide a no-arg call method for the instance.
# E.g. if a class defines GetState and you'd like to be able to call
# self.GetState() from within the class, do this instead:
#
#   class Foo(object):
#     def __init__(self):
#       self.GetState  = self.
