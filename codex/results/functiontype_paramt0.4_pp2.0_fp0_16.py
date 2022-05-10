from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'add_one')(i) for i in range(3))

# list(map(add_one, range(3)))

# lambda: None
# lambda x: x
# lambda x, y: x + y
# lambda x, y, z: x + y + z
# lambda *args: sum(args)
# lambda **kwargs: sum(kwargs.values())
# lambda x, *, y=0, z=0: x + y + z

# def func_with_keyword_only_arg(*, arg):
#     return arg
# func_with_keyword_only_arg(arg=1)
# func_with_keyword_only_arg(1)

# def func_with_keyword_only_arg(*, arg=None):
#     return arg
# func_with_keyword_only_arg()
# func_with_keyword_only_arg(arg=1)
# func_with_keyword_only_arg(1)

# def func_with_keyword
