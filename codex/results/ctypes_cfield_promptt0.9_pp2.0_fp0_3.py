import ctypes
# Test ctypes.CField() and _ctypes_test.fillfloatarr() both.
import _ctypes_test
ll = ctypes.cdll.LoadLibrary(None)
cdoublep = ctypes.POINTER(ctypes.c_double)
ll.fillfloatarr.argtypes = (cdoublep, ctypes.c_int)
ll.fillfloatarr.restype = None
buf = (ctypes.c_double * 10)()
ll.fillfloatarr(buf, len(buf))
buf,

#with ctypes.CDLL(None) as lib:
#	ll.fillfloatarr.argtypes = (cdoublep, ctypes.c_int)
#	ll.fillfloatarr.restype = None
#	
# Test ctypes.CDLL() and its created dlls.
print 'sys.platform', sys.platform
fname = 'ctypes_test_dll.dll'
try:
	dll = ctypes.CDLL(fname)
	print 'CDLL(%s) ok.' % (fname)
except:
	try:
		dll =
