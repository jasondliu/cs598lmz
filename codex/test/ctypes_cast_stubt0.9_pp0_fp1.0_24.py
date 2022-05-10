import ctypes
ctypes.cast(1, ctypes.c_void_p)

class renderstate_base_t(ctypes.Structure):
    _fields_ = [('cullMode', ctypes.c_uint), ('flags', ctypes.c_uint), ('shadowPassIndex', ctypes.c_int)]

renderstate_base_t.cullMode

s = str(renderstate_base_t)
