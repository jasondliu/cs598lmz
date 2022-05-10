from types import FunctionType
a = (x for x in [1])
EXCEPTION(a, TypeError("'generator' object does not support item assignment"))
b = {'a':4,'b':5}
EXCEPTION(b, TypeError("'dict' object does not support item assignment"))
def c(a): return a+1
EXCEPTION(c, TypeError("'function' object does not support item assignment"))
class d: pass
EXCEPTION(d, TypeError("'classobj' object does not support item assignment"))
EXCEPTION((1,2,3), TypeError("'tuple' object does not support item assignment"))
EXCEPTION("abc", TypeError("'str' object does not support item assignment"))
EXCEPTION(True, TypeError("'bool' object does not support item assignment"))
EXCEPTION(1, TypeError("'int' object does not support item assignment"))
EXCEPTION(1j, TypeError("'complex' object does not support item assignment"))
EXCEPTION(1.0, TypeError("'float' object does not support item assignment"))
EXCEPTION(u"abc", TypeError("'unicode' object
