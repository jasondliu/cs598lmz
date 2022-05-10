from types import FunctionType
list(FunctionType(lambda:range(10)))

del x
f()
 
s=s[:-1]+', more prgs, more prgs so'
from swidgets import *

 
from types import ModuleType

def find_modules(moduletree, package=""):
    for elt in moduletree.__dict__.keys():
        module_ = getattr(moduletree, elt)
        if type(module_) is ModuleType:
            yield package+module_.__name__
        else:
            if not (elt.startswith("_") or hasattr(module_, "__module__")):
                yield from find_modules(module_, package+module_.__name__+".")

x=list(find_modules(swidgets))
x.sort()
" ".join(x)

#print(__import__('smultilist').__file__)
#print(__import__('smultilist').__doc__)
#print(repr(__import__('smultilist').__spec__))

import swidgets
def
