from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__.items())

# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1026017f0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/jdong/PycharmProjects/tl_py/dong/set/global/global_local.py', '__cached__': None, 'x': 5}

# 其中 __globals__ 中的__builtins__是自带的，默认就会有的
# __spec__ 是描述符，也就是说__spec__的属性可以用来描述变量的

import sys
# sys.__spec
