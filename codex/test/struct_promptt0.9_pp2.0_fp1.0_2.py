import _struct
# Test _struct.Struct
def test_Constructor_Parameterized():
    """_struct.Struct(format[, name])"""
    Struc = _struct.Struct
    s = Struc('i')
    assert repr(s) == "Struct('i')"
    s = Struc('b','nameHere')
    assert repr(s) == "Struct('b','nameHere')"
    #
    s = Struc()
    try: s = Struc('')
    except ValueError: pass
