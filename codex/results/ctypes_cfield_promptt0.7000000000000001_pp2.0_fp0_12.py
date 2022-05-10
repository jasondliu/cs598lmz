import ctypes
# Test ctypes.CField.
import ctypes.test

# Test ctypes.util.find_library
if 'linux' in sys.platform:
    ctypes.util.find_library('m')

# Test ctypes.util.find_msvcrt
if ctypes.util.find_msvcrt() is not None:
    ctypes.cdll.msvcrt

# Test ctypes.util.find_library, again
ctypes.CDLL(ctypes.util.find_library("m"))

# Test that ctypes.__version__ is set
try:
    ctypes.__version__
except AttributeError:
    print "test_ctypes failed: __version__ not defined"
    sys.exit(-1)

test_support.run_unittest(test_ctypes, test_lazy_loader, test_structseq)
test_support.reap_children()
