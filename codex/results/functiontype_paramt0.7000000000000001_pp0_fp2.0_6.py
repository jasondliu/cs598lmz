from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

## [0]

#f.__code__.co_freevars

## ('y',)

#f.__closure__

## (<cell at 0x7f5c5ff7d2b0: int object at 0x7f5c6005a5e0>,)

#f.__closure__[0].cell_contents

## 2

#f.__globals__

## {'__builtins__': <module '__builtin__' (built-in)>, '__file__': '<stdin>', 'f': <function f at 0x7f5c60019f50>, '__name__': '__main__', '__package__': None, '__doc__': None}

#f.__globals__['__builtins__'].__dict__['__import__']

## <built-in function __import__>

#f.__gl
