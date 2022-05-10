import types
# Test types.FunctionType, FunctionType instances don't have a stack_size attr
try:
    FunctionType = types.FunctionType
    raise TestFailed, "did not raise TypeError on FunctionType.stack_size"
except AttributeError:
    pass

# Test types.GeneratorType, GeneratorType instances don't have a stack_size
# attr
class Generator:
    def __init__(self):
        self.gi_frame = sys._getframe()
try:
    GeneratorType = types.GeneratorType
    raise TestFailed, "did not raise AttributeError on GeneratorType.stack_size"
except AttributeError:
    pass
try:
    GeneratorType.f_stack_size(Generator())
    raise TestFailed, "did not raise AttributeError on Generator.stack_size"
except AttributeError:
    pass

def raise_exception():
    raise RuntimeError, "oh no!"

frame = raise_exception.func_code.co_firstlineno + 1
raise_exception.func_code.co_firstlineno = sys.maxint

