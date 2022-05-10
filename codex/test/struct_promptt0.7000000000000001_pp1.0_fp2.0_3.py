import _struct
# Test _struct.Struct()
def test_Struct():
    # verify fmt
    raises(TypeError, _struct.Struct)
    raises(TypeError, _struct.Struct, None)
    raises(TypeError, _struct.Struct, 'xx')
    raises(TypeError, _struct.Struct, '1s')
    raises(TypeError, _struct.Struct, '1s2s')
    raises(TypeError, _struct.Struct, '1s2s3s')
    raises(TypeError, _struct.Struct, '1s2s3s4s')
    raises(TypeError, _struct.Struct, '1s2s3s4s5s')
    raises(TypeError, _struct.Struct, '1s2s3s4s5s6s')
    raises(TypeError, _struct.Struct, '1s2s3s4s5s6s7s')
    raises(TypeError, _struct.Struct, '1s2s3s4s5s6s7s8s')
