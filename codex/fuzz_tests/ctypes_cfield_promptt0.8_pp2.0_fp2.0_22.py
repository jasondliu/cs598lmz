import ctypes
# Test ctypes.CField class
class _fluid_core_t(ctypes.Structure):
    _fields_ = [('L', ctypes.c_int32), ('N', ctypes.c_int32)]
    
#
# Test ctypes.CArray class
#

#
# Test ctypes.CPointer class
#

#
# Test ctypes.CFunctionPtr class
#

#
# The following tests involve structs
#

#
# Test ctypes.CStruct class
#
class _fluid_settings_t(ctypes.Structure):
    _fields_ = [('min_gain', ctypes.c_double), ('max_gain', ctypes.c_double)]

class _fluid_synth_t(ctypes.Structure):
    _fields_ = [('core', _fluid_core_t),
                ('settings', _fluid_settings_t)]

# Test CStruct.__init__ method
def test_constructor():
    # Create a couple of structs
    core = _fluid_core_t()
    core
