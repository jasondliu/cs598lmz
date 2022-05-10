import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_float, ctypes.POINTER(ctypes.c_float))

# Get the address of the function
df_fn = ctypes.cast(dF.ctypes.data, ctypes.POINTER(ctypes.c_float))

# Make a function that can be called by ctypes
dF_fn = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.POINTER(ctypes.c_float))(df_fn)

# Test the function
dF_fn(ctypes.byref(ctypes.c_float(3.14)))

#%%
# Test ctypes.CFUNCTYPE(ctypes.c_float, ctypes.POINTER(ctypes.c_float), ctypes.c_float, ctypes.c_float)

# Get the address of the function
sh_fn = ctypes.cast(shear.ctypes.data, ctypes.POINTER(ctypes.c_float))

# Make a function that can be called by ctypes
shear_fn = ctypes.
