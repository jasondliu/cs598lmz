import _struct
import _array
import _collections
import _utilities

def test__struct(test_harness):
    test_harness.checkComplainAndAdjustExpected( 0)

    struct_object = _struct.Struct( "3i")
    test_harness.test( struct_object.create( 1, 2, 3), bytearray( b'\x01\x00\x00\x00'
                                                                 + b'\x02\x00\x00\x00'
                                                                 + b'\x03\x00\x00\x00'
                                                                 + b'\x00\x00\x00\x00'
                                                                 + b'\x00\x00\x00\x00'
                                                                 + b'\x00\x00\x00\x00'
                                                                 + b'\x00\x00\x00\x00'
                                                                 + b'\x00\x00\x00\x00'
                                                                 + b'\
