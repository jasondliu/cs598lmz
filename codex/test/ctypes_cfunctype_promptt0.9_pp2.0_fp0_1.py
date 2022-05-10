import ctypes
# Test ctypes.CFUNCTYPE
def delete(fn):
	image_to_delete = ( ctypes.c_ubyte * fn ).in_dll(dll, 'Image')
	image_to_delete = 0
	return

