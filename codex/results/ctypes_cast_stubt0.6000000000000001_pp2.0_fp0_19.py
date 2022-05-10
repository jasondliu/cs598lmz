import ctypes
ctypes.cast(ctypes.pointer(a), ctypes.POINTER(ctypes.c_int))
</code>
But I have no idea how to convert that to a numpy array. 
Does anyone know how to do this?
Thanks!


A:

You can do that with the <code>ctypes</code> module.
<code>import ctypes

a = np.array([1,2,3,4])
shared_array = a.__array_interface__['data'][0]

# Convert the pointer to a ctypes pointer:
shared_array_ctypes = ctypes.POINTER(ctypes.c_int)(shared_array)

# Create a numpy array using the pointer:
b = np.ctypeslib.as_array(shared_array_ctypes, (4,))
</code>
You can also write to the array using the <code>ctypes</code> pointer:
<code>shared_array_ctypes[2] = 42

print a
# array([ 1,  2, 42,  4])
</code>

