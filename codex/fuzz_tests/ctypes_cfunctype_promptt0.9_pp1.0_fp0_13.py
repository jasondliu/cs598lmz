import ctypes
# Test ctypes.CFUNCTYPE declaration...
CFUNCTYPE = ctypes.CFUNCTYPE
char_p = ctypes.POINTER(ctypes.c_char)
sentinel = ctypes.c_int.in_dll(ctypes.pythonapi, 'PyErr_CheckSignals').argtypes[0]
# ...and underlying C function implementation.
@CFUNCTYPE(ctypes.c_int, sentinel)
def NeverReturn(sentinel):
    return 0
orig_check_signals = ctypes.pythonapi.PyErr_SetInterrupt # orig func
if orig_check_signals(NeverReturn(num_ticks)) != 0:
    raise RuntimeError('Wrapping PyErr_CheckSignals failed!')
# Test that we haven't crashed:
print 'PyErr_CheckSignals wrapped; will now print for %d ticks' % num_ticks
sys.stdout.flush()
# So we shouldn't see any "KeyboardInterrupt"...
try:
    for i in xrange(num_ticks):
        sleep(1)
        print 'clock ticks
