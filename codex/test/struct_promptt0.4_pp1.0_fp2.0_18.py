import _struct
# Test _struct.Struct()

def test_struct_error():
    raises(TypeError, _struct.Struct)
    raises(TypeError, _struct.Struct, 'abc', 'def')
    raises(TypeError, _struct.Struct, 'abc', 'def', 'ghi')
    raises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl')
    raises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl', 'mno')
    raises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr')
    raises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr',
           'stu')
    raises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr',
           'stu', 'vwx')
