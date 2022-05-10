from types import FunctionType
list(FunctionType(None,(),{}).__new__(FunctionType))
# [None, ()]

# Fix for funcs that don't accept kwargs
# See
# http://docs.python.org/library/functions.html#func_new
# http://docs.python.org/reference/datamodel.html#object.__new__
class Dummy:
    pass
dummy = Dummy()
dummy.__new__ = None
dummy.__init__ = None
list(dummy.__new__(Dummy))
# [None]
list(dummy.__new__(Dummy,None))
# [None, None]
list(dummy.__new__(Dummy,None,None))
# [None, None, None]
'''
