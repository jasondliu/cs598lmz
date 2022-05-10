from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# [('__annotations__', {}),
#  ('__call__', <method-wrapper '__call__' of function object at 0x7f0d5d5b5e18>),
#  ('__closure__', None),
#  ('__code__', <code object <lambda> at 0x7f0d5d5b5ea0, file "<stdin>", line 1>),
#  ('__defaults__', None),
#  ('__get__', <method-wrapper '__get__' of function object at 0x7f0d5d5b5e18>),
#  ('__globals__', {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f0d5d5b5c88>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in
