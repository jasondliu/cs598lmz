import types
# Test types.FunctionType
class C:
    def f(self):
        return "f"

x = C()
print type(x.f) is types.FunctionType
print type(C.f) is types.FunctionType
print type(C) is types.ClassType
# Test types.MethodType
print type(x.f) is types.MethodType
print type(C.f) is types.MethodType

# Test types.MethodType
from types import MethodType

class C:
    def f(self):
        return "f"

x = C()

print type(x.f) is MethodType
print type(C.f) is MethodType

# Test types.InstanceType
from types import InstanceType

class C:
    def f(self):
        return "f"

x = C()

print type(x) is InstanceType

# Test types.UnboundMethodType
from types import UnboundMethodType

class C:
    def f(self):
        return "f"

x = C()

print type(x.f)
