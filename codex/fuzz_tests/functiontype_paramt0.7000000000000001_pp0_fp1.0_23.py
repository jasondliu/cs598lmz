from types import FunctionType
list(FunctionType(lambda:1))

# Code of __init__ method in list
class list():
    def __init__(self, *args, **kwargs):
        if not args:
            return
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        if not hasattr(args[0], '__iter__'):
            raise TypeError(
                "list() argument must be iterable, not '%s'" % type(args[0]).__name__)
        self.extend(args[0])

# How to generate a list of numbers
list(range(1, 7))

# How to unpack a list of numbers
a, b = [1, 2]

# Is there a way to list all the attributes of a list?
dir(list)

# How to create a list of dictionaries
[{} for _ in range(10)]

# How to create a list of dictionaries where each item is actually a reference to the same dictionary
[{}] * 10

# How to create a
