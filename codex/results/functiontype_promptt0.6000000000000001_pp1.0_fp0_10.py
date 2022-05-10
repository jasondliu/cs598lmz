import types
# Test types.FunctionType
func = types.FunctionType(code, globals(), 'func')
func()
# Test types.BuiltinFunctionType
def test_builtin(f):
    if isinstance(f, types.BuiltinFunctionType):
        print("pass")

test_builtin(test_builtin)
# Test types.MethodType
class A:
    def __init__(self, name):
        self.name = name
    def say(self):
        print("hello", self.name)

a = A('sito')
m = types.MethodType(code, a, A)
m()

# Test types.ModuleType
module_name = 'test_module'
m = types.ModuleType(module_name)
setattr(m, 'x', 1)
setattr(m, 'func', func)

# Test types.TracebackType
try:
    raise ValueError('test')
except ValueError as e:
    tb = e.__traceback__
    print(type(tb))

# Test types.FrameType
frame = tb
