from types import FunctionType
list(FunctionType(lambda a: a, {}).__code__.co_varnames)

#

class EchoClass:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return str(self.arg)


def echo_func(arg):
    return arg


def echo_function(func):
    return func


echo_function(echo_func)(EchoClass(123))

#

lambda x: x + 1

y = 1
f = lambda x: x + y
f(3)

#

list(map(lambda x: x ** 2, range(5)))

#

list(filter(lambda x: x % 2 == 0, range(10)))

#

list(zip([1, 2, 3, 4], [5, 6, 7, 8]))

#

dict(zip(['a', 'b', 'c', 'd'], [5, 6, 7, 8]))


#

def make_incrementor(n):
    return lambda x:
