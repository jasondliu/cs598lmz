import ctypes
# Test ctypes.CField

# <codecell>

class layout_t(ctypes.Structure):
    _fields_ = [
        # Required fields
        ("name", ctypes.c_char_p),
        ("width", ctypes.c_uint),
        ("depth", ctypes.c_uint),
        ("height", ctypes.c_uint),
        ("layout_type", ctypes.c_char_p),
        ("power", ctypes.c_double),
        ("area", ctypes.c_double),
        # Optional fields
        ("leakage", ctypes.c_double),
        ("peak_dynamic", ctypes.c_double),
        ("runtime", ctypes.c_double),
        ("runtime_dynamic", ctypes.c_double),
        ("runtime_leakage", ctypes.c_double),
        ("runtime_short_circuit", ctypes.c_double),
        ("runtime_long_circuit", ctypes.c_double),
        # Custom fields
        ("num_regs", ctypes.c_uint),
        ("
