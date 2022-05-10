import _struct
# Test _struct.Struct is working. This must be
# done before importing _MockArray
_struct.Struct('d').unpack('\x00'*8)
# Test _MockArray is working. This must be
# done before importing _MockMeasure
from _MockArray import MockArray
# Test _value_to_mock is working. This must be
# done before importing _MockMeasure
from _MockArray import _value_to_mock
# Test _MockMeasure is working. This must be
# done before importing _MockMeasureByValue
from _MockMeasure import MockMeasure
# Test _MockMeasureByValue is working. This must be
# done before importing _utils
from _MockMeasureByValue import MockMeasureByValue
# Test _utils is working. This must be
# done before importing _Device
from _utils import int_to_bytearray
# Test _Device is working. This must be
# done before importing this module.
from _Device import Device

class MockDevice(Device):
	"""A mock class for testing the Device class."""
