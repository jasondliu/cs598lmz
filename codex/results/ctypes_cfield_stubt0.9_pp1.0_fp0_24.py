import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

pyo = py.test.importorskip('pypy._pypy.lib_pypy')
af = pyo.cpyext_api.load_extension_module('funct', 'cpyext')
S2 = af.new_S()

def check(text, expected_result, expected_text):
    assert af.check_CField(expected_result)
    assert af.check_CField_personality(expected_text)

def test_simple():
    import pypy.module._cffi_backend.newtype
    from pypy.module._cffi_backend import ctypeobj
    check(S.x, ctypeobj.W_CType.from_ctype(S.x),
          pypy.module._cffi_backend.newtype.get_base_ctype(S.x).name)
    check(S2.x, ctypeobj.W_CType.from_ctype(S2.x),
          pypy.module._cffi_backend.
