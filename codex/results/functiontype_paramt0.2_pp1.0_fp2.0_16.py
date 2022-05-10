from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# The following code shows how to use the inspect module to get the names of the arguments of a function.

import inspect
def foo(a, b, c):
    pass
inspect.getargspec(foo)

# ArgSpec(args=['a', 'b', 'c'], varargs=None, keywords=None, defaults=None)

# The following code shows how to use the inspect module to get the names of the arguments of a method.

import inspect
class Foo(object):
    def bar(self, a, b, c):
        pass
inspect.getargspec(Foo.bar)

# ArgSpec(args=['self', 'a', 'b', 'c'], varargs=None, keywords=None, defaults=None)

# The following code shows how to use the inspect module to get the names of the arguments of a lambda function.

import inspect
inspect.getargspec(lambda a, b, c: None)

# ArgSpec(
