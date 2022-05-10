import ctypes
ctypes.cast(ctypes.c_void_p(0x12345678), ctypes.POINTER(ctypes.c_int))

#%%
import ctypes
ctypes.cast(ctypes.c_void_p(0x12345678), ctypes.POINTER(ctypes.c_int))[0]

#%%
import ctypes
ctypes.cast(ctypes.c_void_p(0x12345678), ctypes.POINTER(ctypes.c_int))[0] = 0x12345678

#%%
import ctypes
ctypes.cast(ctypes.c_void_p(0x12345678), ctypes.POINTER(ctypes.c_int))[0] = 0x12345678

#%%
import ctypes
ctypes.cast(ctypes.c_void_p(0x12345678), ctypes.POINTER(ctypes.c_int))[0] = 0x12345678

#%%
import ctypes
ctypes.cast(ctypes.c_void_p(0x12345678),
