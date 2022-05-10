from types import FunctionType
list(FunctionType(lambda:0).__globals__.keys())
# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'types']
# >>> 
# >>> FunctionType(lambda:0).__globals__['__name__']
# '__main__'
# >>> FunctionType(lambda:0).__globals__['__file__']
# '<stdin>'
# >>> FunctionType(lambda:0).__globals__['__spec__']
# ModuleSpec(name='__main__', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7f3b3e80a080>, origin='<stdin>', submodule_search_locations=None)
# >>> 
# >>> FunctionType(lambda:0).__globals__['__spec__'].name
# '__main__'
# >>> FunctionType(lambda:0).__globals__['__spec__'].loader
