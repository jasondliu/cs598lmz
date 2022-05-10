import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 3

class T(ctypes.Structure):
    x = ctypes.c_char * 2

def test_cast():
    source = S()
    source.x = 'xxx'
    target = cast(pointer(source), POINTER(T))
    assert target.contents.x == 'xx'

def test_byref():
    source = S()
    source.x = 'xxx'
    target = byref(source)
    assert target.contents.x == 'xxx'

def test_addressof():
    source = S()
    source.x = 'xxx'
    assert addressof(source) != None

def test_alignment():
    assert alignment(S) == 1

def test_string_at():
    source = S()
    source.x = 'xxx'
    target = byref(source)
    assert string_at(target) == 'xxx'

def test_wstring_at():
    source = ctypes.wchar_p(u'xxx')
    assert wstring
