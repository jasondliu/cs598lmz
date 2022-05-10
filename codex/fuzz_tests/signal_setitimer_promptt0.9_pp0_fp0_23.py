import signal
# Test signal.setitimer() and the ITIMER_REAL timer,
# because it works on Linux, where it is safe, and on MacOS,
# where it gives you a temporary workaround.  You can run test_itimer_real
# manually on Solaris or FreeBSD to see that it fails.
try:
    import signal
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
    setitimer_works = True
except (ImportError, AttributeError):
    setitimer_works = False
#
# Test whether the settypeof() method of arrays needs to be called to
# initialize the array type.
needs_setflags = True
try:
    import numpy.core.multiarray as _numpymultiarray
    needs_setflags = hasattr(_numpymultiarray, '_get_ndarray_c_version')
except ImportError:
    pass

# Convert an integer object to a C void*/intptr_t, calling PyLong_AsVoidPtr
# if the machine is 64-bit.  On other machines the integer must be in valid
