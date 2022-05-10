from types import FunctionType
list(FunctionType(lambda: 1, globals()).__closure__)

#import inspect
#inspect.getsource(FunctionType(lambda: 1, globals()))

#"""
#>>> def f():
#...     a = 1
#...     b = a + 1
#...     print(b)
#...
#>>> f()
#2
#>>> f.__code__.co_freevars
#('a',)
#>>> f.__closure__
#(<cell at 0x7f07c482e018: int object at 0x7f07c4c4d4a8>,)
#>>> f.__closure__[0].cell_contents
#1
#"""

#"""
#>>> def f():
#...     a = 1
#...     b = a + 1
#...     print(b)
#...
#>>> f()
#2
#>>> f.__code__.co_freevars
#('a',)
#>>> f.__closure__
#(<cell at 0x7f07c482e018: int object
