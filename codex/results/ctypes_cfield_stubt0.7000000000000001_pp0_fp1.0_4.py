import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_get_index():
    assert S.x.get_index() == 'x'

def test_get_index_for_name():
    assert S.get_index_for_name('x') == 'x'

def test_get_targets():
    assert S.x.get_targets() == []

def test_get_targets_for_name():
    assert S.get_targets_for_name('x') == []

def test_get_structure():
    assert S.x.get_structure() is S

def test_get_structure_for_name():
    assert S.get_structure_for_name('x') is S

def test_get_type():
    assert S.x.type is ctypes.c_int

def test_get_type_for_name():
    assert S.get_type_for_name('x') is ctypes.c_int

def test_get_offset():
    assert S.x.offset == 0

def test_
