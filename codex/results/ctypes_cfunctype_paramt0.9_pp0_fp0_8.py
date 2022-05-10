import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_double)
def std_print(x):
	print x

# Now the variadic declaration
fun = FUNTYPE(None)

# This should raise an exception
try:
	fun(1,"test",2,3,std_print)
except:
	traceback.print_exc()

# This should print 2 and 3, then call std_print
fun(1,2,3,std_print)

# This should call std_print two times
fun(1,std_print,2,std_print)


print "This is an example of the use of ctypes.Structure:"
class colour(ctypes.Structure):
	_fields_ = (("red", ctypes.c_int),
				("green", ctypes.c_int),
				("blue", ctypes.c_int))

# ctypes.Structure has overloaded the bracket operator.
pvinyl = colour(255, 0, 255)
print "a magenta colour is", pvinyl[0], pvinyl[1], pvin
