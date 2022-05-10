import types
# Test types.FunctionType
def f(): pass
b=types.FunctionType(f.func_code,f.func_globals)
print b
# Test types.BuiltinFunctionType
print types.BuiltinFunctionType(map)

a=types.ClassType(object)
print isinstance(a(),object)

# Test types.UnboundMethodType
import types
class C:
    def foo(self):
        pass
c=C()
print types.UnboundMethodType(c.foo,C,C.__class__)

# Test types.InstanceType
import types
class C:
    def foo(self):
        pass
c=C()
print types.InstanceType(c)

# Test sys.setswitchinterval
import sys
sys.setswitchinterval(2)

# Test sys.getswitchinterval
import sys
print sys.getswitchinterval()

import sys
print sys.getcheckinterval()

import sys
sys.setcheckinterval(2)
print sys.getcheckinterval()

# Test sys.setcheckinterval
import
