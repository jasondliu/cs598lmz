import types
# Test types.FunctionType
F1 = types.FunctionType(code='', globals={})
F2 = types.FunctionType(F1.__code__, {})
F3 = types.FunctionType(F2.__code__, {})
del F1, F2, F3
# Test types.TracebackType
t = types.TracebackType(None)
t.tb_frame
t.tb_lasti
t.tb_lineno
t.tb_next
del t
# Test types.FrameType
t = types.FrameType(None, None, None)
t.f_code
t.f_locals
t.f_back
t.f_globals
del t
# Test types. code
import code
code.__dict__['types']
code.__dict__['_']
code.__dict__['_y']
del code
# Test types. builtins
import builtins
builtins.__dict__['types']
builtins.__dict__['_']
del builtins
