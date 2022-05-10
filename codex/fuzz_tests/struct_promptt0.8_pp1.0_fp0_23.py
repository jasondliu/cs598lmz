import _struct
# Test _struct.Struct() API
def test_struct_api():
    # Some basic sanity tests
    alltesters = []
    for code in range(256):
        try:
            st = _struct.Struct(chr(code))
            if code == _struct.STRUCT_CODES[st.format]:
                alltesters.append(st)
        except ValueError:
            pass
    # Assert that no format code is tested more than once
    assert len(alltesters) == len(_struct.STRUCT_CODES)
    # Use all testers on some values
    for tester in alltesters:
        testelem = _struct.pack(tester.format, -3.14)
        testvalue = _struct.unpack(tester.format, testelem)[0]
        assert tester.size == len(testelem)
        assert testvalue == -3.14
    # Struct can handle keyword arguments
    _struct.Struct(format='d')
    # Struct can handle non-string format
    _struct.Struct(b'd')
    # Test that default endianness is native
   
