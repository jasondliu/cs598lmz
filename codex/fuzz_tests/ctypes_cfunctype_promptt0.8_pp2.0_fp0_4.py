import ctypes
# Test ctypes.CFUNCTYPE(None) works
def fn():
    pass
fn_ptr = ctypes.CFUNCTYPE(None)(fn)
fn_ptr()
</code>

