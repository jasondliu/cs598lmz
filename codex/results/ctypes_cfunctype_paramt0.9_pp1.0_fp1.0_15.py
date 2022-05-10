import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long)
libNotify.FileCopy.restype = ctypes.c_char_p
libNotify.FileCopy.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long]

@FUNTYPE
def FileProgress(c_file, c_target, c_done):
	done = c_done / 1024.0
	size = os.path.getsize(c_file) / 1024.0
	target = c_target
	shutil.copy2(c_file, target)
	return True

def FileCopy(source, target):
	progress = FileProgress
	progress = FUNTYPE(progress)
	ret = libNotify.FileCopy(source, target, progress)
	if ret == False:
		raise Exception('FileCopy: %s -> %s fail!'%(source, target))
	return ret

def FileCopyWithCallback(source, target, callback, small
