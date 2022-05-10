import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(a):
	print "callback(%d)" % a
	return a+1

cb = FUNTYPE(callback)

print "calling cb(42)"
print "cb(42) = %d" % cb(42)
