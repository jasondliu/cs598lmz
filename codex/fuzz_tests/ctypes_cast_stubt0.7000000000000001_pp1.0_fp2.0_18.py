import ctypes
ctypes.cast(x, ctypes.py_object).value

#numpy.frombuffer(x, dtype=numpy.complex64)

#x = numpy.fromstring(x, dtype=numpy.complex64)



from array import array
x=array('f',x)
print x
print x[7]
print len(x)
#x=numpy.array(x)
x=x.tolist()
#print x


#from numpy import *
#from numpy.core.multiarray import frombuffer
#
#x.tostring()
#x_arr = frombuffer(x, dtype=float32)
#print x_arr
#
#from numpy import *
#from numpy.core import *
#x_arr = frombuffer(x, dtype=float32)
#print x_arr
#
#
#from numpy import *
#from numpy.core.multiarray import frombuffer
#
#from StringIO import StringIO
#
#s = StringIO(x)
#print frombuffer(
