fn = lambda: None
# Test fn.__code__
#   | fn.__code__
#   |   | fn.__code__.__dict__
#
# Test fn.__dict_()
#   | fn.__dict__
#   |   | fn.__dict__.__class__ # <type 'dict'>
#   |   | fn.__dict__.__defaults__ # None
#   |   | fn.__dict__.__get__ # <slot wrapper '__get__' of 'method' objects>
#   |   | fn.__dict__.__items__() # [('__name__', 'fn'), ('__doc__', None)]
#   |   | fn.__dict__.__members__ # {'__getitem__', '__reduce_ex__', '__setitem__', '__doc__', '__dict__', '__repr__', '__format__', '__init__', 'pop', 'popitem', 'update', 'copy', 'setdefault', '__str__', '__reduce__', 'get', 'keys', 'items', 'clear', '__contains__',
