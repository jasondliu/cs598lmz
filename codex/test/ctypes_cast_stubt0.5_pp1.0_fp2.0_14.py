import ctypes
ctypes.cast(0, ctypes.py_object)

# ____________________________________________________________

def test_nop():
    pass

def test_string():
    return "hello"

def test_tuple():
    return (1, 2, 3)

def test_list():
    return [1, 2, 3]

def test_dict():
    return {1: 2, 3: 4}

def test_set():
    return set([1, 2, 3])

def test_frozenset():
    return frozenset([1, 2, 3])

def test_unichr():
    return unichr(1234)

def test_unicode():
    return u"hello"

