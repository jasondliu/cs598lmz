import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_get_set_item():
    s = S()

    # set
    s[0] = 42
    assert s.x == 42

    # get
    assert s[0] == 42

def test_get_set_item_slice():
    s = S()

    # set
    s[0:] = 42
    assert s.x == 42

    # get
    assert s[0:] == 42

    # set
    s[:] = 43
    assert s.x == 43

    # get
    assert s[:] == 43

    # set
    s[::] = 44
    assert s.x == 44

    # get
    assert s[::] == 44


def test_getset_item_slice_range():
    s = S()

    # set
    s[:1] = 42
    assert s.x == 42

    # get
    assert s[:1] == 42

    # set
    s[:2] = 42
    assert s.x == 42

    # get
    assert s[:2] ==
