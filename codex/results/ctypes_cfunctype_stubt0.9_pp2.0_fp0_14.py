import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ""

class C:
    def __init__(self):
        self.f = fun
        self.g = self._g
    def _g(self):
        return ""

x = C()
print(dir(x))
</code>
output:
<code>['_C__g', '_C__init__', '_CFuncPtr__call__', '_CFuncPtr__slots_', '_CFuncPtr__write_ptr__', '_CFuncPtr__write_proto__', '_CFuncPtr_argtypes', '_CFuncPtr_errcheck', '_CFuncPtr_flags', '_CFuncPtr_func', '_CFuncPtr_restype', '_CFuncPtr_use_errcheck', '_CFuncPtr_value', '__doc__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__objclass__', '__reduce__', '__reduce_ex__', '__repr__', '__str__', &lt;class 'ctypes.
