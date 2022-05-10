import ctypes
# Test ctypes.CFUNCTYPE
def delete(fn):
	image_to_delete = ( ctypes.c_ubyte * fn ).in_dll(dll, 'Image')
	image_to_delete = 0
	return

def open_image(fn):	
	# class IMAGE_T(ctypes.Structure):
	# 	_fields_ = [("file_name", ctypes.POINTER(ctypes.c_ubyte)),
	# 				("file_name_length", ctypes.c_int),
	# 				("height", ctypes.c_int),
	# 				("width", ctypes.c_int),
	# 				("num_colors", ctypes.c_int),
	# 				("pixels", ctypes.POINTER(ctypes.c_ubyte))]

	# class IMAGE_T(ctypes.Structure):
	# 	_fields_ = [("file_name_length", ctypes.c_int),
	# 			
