import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

def foo(x):
	print("hi")

print("foo is type", type(foo), "and has address", id(foo))

f = FUNTYPE(foo)
print("f is type", type(f), "and has address", id(f))

print("Calling f(3)")
f(3)

print("Binding f to bar")
bar = f
print("bar is type", type(bar), "and has address", id(bar))

print("Calling bar(3)")
bar(3)

print("Binding f to baz")
baz = f
print("baz is type", type(baz), "and has address", id(baz))

print("Calling baz(3)")
baz(3)

print("Changing f to refer to a new function")
def newfoo(x):
	print("newfoo")
f = FUNTYPE(newfoo)
print("f is type", type(f), "and has address", id(f))


