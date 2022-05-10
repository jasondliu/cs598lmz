from types import FunctionType
list(FunctionType(lambda x: x, globals()).__globals__.items())

# [('__name__', '__main__'), ('__doc__', None), ('__package__', None), ('__loader__', <_frozen_importlib_external.SourceFileLoader object at 0x7f8a1a7d7d30>), ('__spec__', None), ('__annotations__', {}), ('__builtins__', <module 'builtins' (built-in)>), ('__file__', './python_data_structures_and_algorithms/fundamental_data_structures/list.py'), ('__cached__', None), ('FunctionType', <class 'type'>)]

# 方法二
import sys
sys._getframe(0).f_globals

# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f8a1a7d7d30>, '__spec__':
