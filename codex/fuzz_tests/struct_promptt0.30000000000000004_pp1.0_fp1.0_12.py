import _struct
# Test _struct.Struct

def test_struct_format():
    # Check that __format__() works.
    s = _struct.Struct("i")
    assert s.__format__("") == "i"
    assert s.__format__("<") == "<i"
    assert s.__format__(">") == ">i"
    assert s.__format__("=i") == "=i"
    assert s.__format__("!") == "!"
    assert s.__format__("<!") == "<!"
    assert s.__format__(">!") == ">!"
    assert s.__format__("=!") == "=!"
    assert s.__format__("=i!") == "=i!"
    assert s.__format__("<i!") == "<i!"
    assert s.__format__(">i!") == ">i!"
    assert s.__format__("!i") == "!i"
    assert s.__format__("!<i") == "!<i"
    assert s.__format__("!>i")
