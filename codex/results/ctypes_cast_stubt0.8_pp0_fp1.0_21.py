import ctypes
ctypes.cast(base_p, ctypes.POINTER(ctypes.c_int32)).contents.value

#This is 2x faster than numpy.frombuffer
base_p = PointerUtils.create_pointer(base, dtype=np.int32)
base_p[1] = np.int32(500)
base_p[0]
base_p[1]

#We can wrap this in a numpy array
base_arr = np.ctypeslib.as_array(base_p, (10,))
base_arr[2] = np.int32(5000)
base_arr
base_p[1]

#This is slower than the numpy.frombuffer
base_arr = np.ctypeslib.as_array(base_p, (10,), require_writable=True)
base_arr
base_arr[2] = np.int32(50000)
base_arr[2]

#This is much much slower
base_p = PointerUtils.create_pointer(base, dtype=np.int32)
base_
