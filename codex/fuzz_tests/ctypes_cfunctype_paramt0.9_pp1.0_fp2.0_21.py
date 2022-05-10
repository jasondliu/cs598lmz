import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.POINTER(NDArrayHandle))
CheckCall(C.MXNDArraySetMonitorCallback(mx_uint(monitor_all),
         FUNTYPE(callback),
         ctypes.c_void_p(0)))
</code>
EDIT: The answer above is wrong. Perferct solution below:
I found a workaround: use cxfloats to get data and call astype() or zeros_like() to convert.
Here is my different attempt which failed:

use ConvertNDArrayToDType returning an array of zeros or an array of
garbage,
use NDArray.asnumpy() returning:


None value when the array is float,

use NDArray.copyto() returning:


an array of 0s when using float array,
None when using int array,


To avoid memory leak, I use ConvertNDArrayToDType and SetNDArrayCtx to retrieve the array from Python after use.

This works for int/float, but not for string. I would never find a way to consume string ndarray from Python.

