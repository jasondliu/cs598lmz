import ctypes
ctypes.cast(lib.getds.argtypes, ctypes.POINTER(myclass)).contents = x

# print x before the call
print "&lt;&lt;&lt; before getds() ====&gt;&gt;&gt;"
print "x.a = ", x.a
print "x.b = ", x.b

# call the function
lib.getds(ctypes.byref(x))

# print x after the call
print "&lt;&lt;&lt; after getds() ====&gt;&gt;&gt;"
print "x.a = ", x.a
print "x.b = ", x.b

# print lib.getds(ctypes.byref(x)).contents
</code>
I think this tries to describe what I want to do. Hope it can be understood clearly.
The problem is that I don't know how to fix this error.

