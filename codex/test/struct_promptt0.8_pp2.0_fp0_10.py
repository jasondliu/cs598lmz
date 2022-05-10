import _struct
# Test _struct.Struct factory
TestError = _struct.error
import weakref

# Some useful structs for testing

# native byte ordering
TestStruct = _struct.Struct('')

# specific byte orderings
TestLE = _struct.Struct('<')
TestBE = _struct.Struct('>')
TestNative = _struct.Struct('=')
TestSTD = _struct.Struct('!')

# alignment
TestAligned4 = _struct.Struct('=iii')
TestAligned2 = _struct.Struct('=HHH')
TestPadded4 = _struct.Struct('=3s')
TestPadded2 = _struct.Struct('=6s')

# packed byte orderings
TestLE_Pack = _struct.Struct('<i')
TestBE_Pack = _struct.Struct('>i')
TestNative_Pack = _struct.Struct('=i')
TestSTD_Pack = _struct.Struct('!i')

# some sample data
