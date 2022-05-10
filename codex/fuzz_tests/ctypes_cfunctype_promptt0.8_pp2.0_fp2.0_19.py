import ctypes
# Test ctypes.CFUNCTYPE(None, ctypes.c_int)
# Test ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int)
# Test ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int) with py3
# Test ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int) with py2
# Test ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int) with py3.3
# Test ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int) with py2.7
#
# All tests should run and raise no exception
#
@pytest.mark.skipif(ctypes is None, reason="Could not import ctypes")
def test_cfunctype(remove_comp_dir, monkeypatch):
    def finalize(compile_dir):
        rbc_path = os.path.join(compile_dir, 'libtest_c
