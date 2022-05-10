from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_freevars)

f = FunctionType(lambda: None, {})
f.__closure__
type(f.__closure__[0].cell_contents)
list(FunctionType(lambda: None, {}).__code__.co_freevars)
f.__closure__[0].cell_contents
f.__closure__[0].cell_contents = 5
f.__closure__[0].cell_contents
 
f = FunctionType(lambda: None, {})
f.__closure__
f.__closure__[0].cell_contents
f.__closure__[0].cell_contents = 5
f.__closure__[0].cell_contents
f.__closure__[0].cell_contents = 'hello'
f.__closure__[0].cell_contents
f.__closure__[0].cell_contents = 5
f.__closure__[0].cell_contents
f.__closure__[0].cell_contents = 'hello'
f.__closure
