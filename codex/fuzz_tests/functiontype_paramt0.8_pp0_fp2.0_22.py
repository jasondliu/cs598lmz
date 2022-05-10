from types import FunctionType
list(FunctionType(haha,globals()).func_closure)

class Test:
    pass
a = Test()
a.__dict__

import sys, types, locale
sys.getrefcount(1)
sys.getrecursionlimit()
sys.getwindowsversion()
sys.maxint
sys.maxsize
types.__dict__
locale.setlocale(locale.LC_ALL,"")
'''
