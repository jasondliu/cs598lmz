import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p)

class CMD(ctypes.Structure):
	_fields_ = [
		('cmd', ctypes.c_ubyte),
		('len', ctypes.c_ubyte),
		('data', ctypes.c_void_p),
	]

class CMD_PACKET(ctypes.Structure):
	_fields_ = [
		('cmd', ctypes.c_ubyte),
		('len', ctypes.c_ubyte),
		('data', ctypes.c_ubyte * 16),
	]

class CMD_RESPONSE(ctypes.Structure):
	_fields_ = [
		('cmd', ctypes.c_ubyte),
		('len', ctypes.c_ubyte),
		('data', ctypes.c_ubyte * 16),
	]

class PARAM(ct
