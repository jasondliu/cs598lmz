import types
# Test types.FunctionType

def f(): pass

def g(): pass

class C:
    def __init__(self):
        self.f = f

c = C()

try:
    types.FunctionType
except:
    print("SKIP")
    raise SystemExit

print(isinstance(f, types.FunctionType))
print(isinstance(g, types.FunctionType))
print(isinstance(c.f, types.FunctionType))
print(isinstance(C, types.FunctionType))
print(isinstance(C.__init__, types.FunctionType))
