import types
# Test types.FunctionType
def f():
    pass
if type(f) != types.FunctionType:
    print("function type error")
# Test types.LambdaType
g = lambda x, y: x+y
if type(g) != types.LambdaType:
    print("lambda type error")
# Test types.GeneratorType
def gen():
    yield 1
if type(gen()) != types.GeneratorType:
    print("generator type error")
# Test types.CodeType
def f():
    pass
if type(f.__code__) != types.CodeType:
    print("code type error")
# Test types.FrameType
def f():
    frame = sys._getframe(0)
    if type(frame) != types.FrameType:
        print("frame type error")
f()
# Test types.TracebackType
def f():
    pass
try:
    f()
except:
    tb = sys.exc_info()[2]
    if type(tb) != types.TracebackType:
        print("traceback type error
