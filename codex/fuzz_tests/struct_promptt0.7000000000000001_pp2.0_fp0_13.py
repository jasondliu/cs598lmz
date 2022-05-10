import _struct
# Test _struct.Struct
import struct
def test_struct_classes():
    def test(fmt, size):
        cls = _struct.Struct(fmt)
        assert issubclass(cls, _struct.Struct)
        assert cls.format == fmt
        assert cls.size == size
        obj = cls()
        assert obj.format == fmt
        assert obj.size == size
        obj = cls(fmt)
        assert obj.format == fmt
        assert obj.size == size
    test('b', 1)
    test('B', 1)
    test('h', 2)
    test('H', 2)
    test('i', 4)
    test('I', 4)
    test('l', 4)
    test('L', 4)
    test('q', 8)
    test('Q', 8)
    test('f', 4)
    test('d', 8)
    test('s10', 10)
    test('P', 8)
    test('P7', 8)
    raises(TypeError, _struct.Struct, 'c')
    raises
