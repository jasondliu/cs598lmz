import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(description, pointer=False):
    # Crashes in full builds of MSVC
    # (crashes in debug builds as well if the asserts in PyObject_Malloc
    #  and PyObject_Free are enabled)
    if description == 'String from None':
        data = ctypes.c_char_p(None)
    elif description == 'String from String':
        data = ctypes.c_char_p(str(42))
    elif description == 'WString from None':
        data = ctypes.c_wchar_p(None)
    elif description == 'WString from String':
        data = ctypes.c_wchar_p(str(42))
    elif description == 'WString from Unicode':
        data = ctypes.c_wchar_p(unicode(42))
    elif description == 'CField from None':
        data = ctypes.CField(None)
    elif description == 'CField from int':
        data = ctypes.CField(42)
    elif description == 'CArray from None
