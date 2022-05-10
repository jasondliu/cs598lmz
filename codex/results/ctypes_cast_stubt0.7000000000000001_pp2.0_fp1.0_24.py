import ctypes
ctypes.cast(buffer, ctypes.POINTER(ctypes.c_int32))

print buffer
</code>
gives me the error:
<code>    ctypes.cast(buffer, ctypes.POINTER(ctypes.c_int32))
TypeError: cannot cast array data from dtype('int64') to dtype('int32')
</code>
I have tried to cast the buffer as a ctypes.c_char_p, but that does not work either.  What is the proper way to do this?


A:

This seems to work fine:
<code>import numpy

array = numpy.arange(10)
print array
buffer = array.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))
print buffer

print ctypes.cast(buffer, ctypes.POINTER(ctypes.c_int32))
</code>

