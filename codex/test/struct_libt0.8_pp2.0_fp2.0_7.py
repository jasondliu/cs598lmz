import _struct
import _array
import _collections
import _utilities

def test__struct(test_harness):
    test_harness.checkComplainAndAdjustExpected( 0)

    struct_object = _struct.Struct( "3i")
