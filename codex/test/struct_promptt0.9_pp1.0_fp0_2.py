import _struct
# Test _struct.Struct compatible objects
def test_struct_compatibility():
    unique_int = 42
    obj = _struct.Struct(unique_int)
    # test str()
    try:
        str(obj)
    except Exception as ex:
        pytest.fail('str() must not raise an Exception, raised: ' + str(ex))
    # test repr()
    try:
        repr(obj)
    except Exception as ex:
        pytest.fail('repr() must not raise an Exception, raised: ' + str(ex))
    # test rich comparison operators
