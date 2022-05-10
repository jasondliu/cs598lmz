import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

def test_create_handle(space):
    w_res = space.appexec([], """():
        from cffi_backend import cdataobj
        cdata = cdataobj.W_CData(42, "int")
        return cdata._handle
    """)
    assert space.int_w(w_res) == 42

def test_create_cdata(space):
    w_res = space.appexec([], """():
        import _cffi_backend
        cdata = _cffi_backend.newp(42, 'int')
        return cdata
    """)
    assert space.int_w(w_res) == 42

def test_create_cdata_array(space):
    w_res = space.appexec([], """():
        import _cffi_backend
        cdata = _cffi_backend.newp_array(42, 'int', 10)
        return cdata
    """)
