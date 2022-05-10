import types
# Test types.FunctionType
print(types.FunctionType)

# Test types.LambdaType
print(types.LambdaType)

# Test types.GeneratorType
def foo():
	yield

g = foo()

print(types.GeneratorType)


# Test types.CodeType
# The code object is immutable
def foo():
	pass
co = foo.__code__
print(types.CodeType)
print(co)
try:
	co.co_filename = "test"
except:
	print("types.CodeType AttributeError")

# Test types.TracebackType
def bar():
	1/0

try:
	bar()
except ZeroDivisionError:
	tb = sys.exc_info()[2]

print(type(tb))
print(types.TracebackType)


# Test types.FrameType
def foo():
	caller_frame = sys._getframe()
	print(caller_frame)
	print(type(caller_frame))

foo()
print(types.FrameType
