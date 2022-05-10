import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)

def _create_callback(func, data):
	return FUNTYPE(func), data

def _set_callback(self, func):
	if not self._callback_set:
		self._callback_set = True
		_lib.vips_image_set_progress(self._pointer, 1)
		_lib.vips_image_set_kill(self._pointer, 1)
	
	self._callback_func = func
	self._callback_data = None
	_lib.vips_image_set_progress_cb(self._pointer, 
		_create_callback(self._callback_handler, self))

def _kill_callback(self, func):
	if not self._callback_set:
		self._callback_set = True
		_lib.vips_image_set_progress(self._pointer, 1)
		_lib.vips_image_set_kill(self._pointer, 1)
	
	
