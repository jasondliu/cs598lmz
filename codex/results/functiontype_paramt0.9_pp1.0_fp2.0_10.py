from types import FunctionType
list(FunctionType(s,globals(),'foop'))
""")

    def test_reduce_bug(self):
        self.assertCodeExecution("""
from types import MethodType
from math import ceil
from builtins import pow

def f(x):
    return x + 1

print("----")
print(f)
print(repr(f))
print("----")
print(MethodType(f, None))
print("----")
e = MethodType(f, None)
try:
    print(repr(e))
    print(e("hello world"))
    print("----")
    print("__reduce__: %r" % (e.__reduce__(),))
    print("__reduce_ex__: %r" % (e.__reduce_ex__(1),))
    print("----")
except TypeError:
    print("TypeError")
print("Finished.")
""")

    def test_unrestricted_unpack(self):
        self.assertCodeExecution("""
from types import MethodType
from math import ceil
