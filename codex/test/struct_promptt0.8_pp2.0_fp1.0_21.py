import _struct
# Test _struct.Struct's str, repr, format and size methods.

def test_struct_basics():
    for code in 'cbB?hHiIlLfd':
        s = Struct(code)
        assert eval(repr(s)) == s
        assert struc
