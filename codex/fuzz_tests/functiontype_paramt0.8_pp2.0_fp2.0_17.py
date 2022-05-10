from types import FunctionType
list(FunctionType(print, globals()))

def f(arg, start=[]):
    start.append(arg)
    return start
list(f(i) for i in range(3))
list(f(i, []) for i in range(3))
list(f(i) for i in range(3))
list(f(i) for i in range(3))
list(f(i) for i in range(3))

# The following attempt is a typical example of what not to do:
def f(arg, start=[]):
    return start
list(f(i) for i in range(3))

class C:
    def __init__(self, arg):
        self._f = arg

c = C([])
c._f
del c._f
c._f
c._f.append(3)
c._f

# Example of a metaclass
class C:
    def meth1(self):
        return 'meth1'
    meth2 = classmethod(lambda cls: 'meth2')
    meth3 = staticmethod(
