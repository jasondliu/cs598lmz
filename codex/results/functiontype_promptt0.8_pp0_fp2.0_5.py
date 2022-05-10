import types
# Test types.FunctionType
def f():
    pass
types.FunctionType(f.func_code, f.func_globals, 'funcname', f.func_defaults, f.func_closure)
# Test types.MethodType
class c:
    pass
def f():
    pass
types.MethodType(f.func_code, c(), c)
# Test types.TypeType
class Class:
    pass

def f():
    pass

types.TypeType(f.func_code, f.func_globals, 'TypeName')

def g():
    pass

types.TypeType(f.func_code, f.func_globals, 'TypeName', (object,))

def h():
    pass

types.TypeType(f.func_code, f.func_globals, 'TypeName', (object, Class))

def i():
    pass

types.TypeType(f.func_code, f.func_globals, 'TypeName', [object, Class])

# Test types.MethodType, types.ClassType

