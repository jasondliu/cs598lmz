fn = lambda: None
# Test fn.__code__.co_firstlineno
#fn.__code__.co_firstlineno

#def f(): return 1
#print(f.__name__); print(f.__code__.co_firstlineno)

import math
import dis
print(dis.dis(math.cos))

#fullargspec(fn)   dis.dis(xxx)
#inspect.getfullargspec(fn) inspect.getsource(fn) inspect.getclasstree(list)

import inspect
print(inspect.getsource(math.cos))
print(inspect.getfile(math.cos))
print(inspect.getmodule(math.cos))


# def show(a = 5, *args, **kwargs):
#     print(a); print(args); print(kwargs)
# print(inspect.getfullargspec(show))
# print(dis.dis(show))


class People(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def say(self,
