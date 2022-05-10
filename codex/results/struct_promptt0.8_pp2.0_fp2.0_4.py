import _struct
# Test _struct.Struct

_STRING_TYPES = (bytes, str)

def getname(obj):
    '''Get the name of an object.'''
    name = getattr(obj, '__name__', None)
    if name is None:
        name = getattr(obj, '__class__').__name__
    return name

def getsize(obj):
    '''Get the size of an object.'''
    size = getattr(obj, 'size', None)
    if size is None:
        size = getsize(getattr(obj, '__class__'))
    return size

class _TestStruct(unittest.TestCase):

    def test_bool(self):
        # Bug #527001: pack/unpack bool value
        b1 = _struct.pack('>?', True)
        self.assertEqual(b1, b'\x01')
        b2 = _struct.pack('>?', False)
        self.assertEqual(b2, b'\x00')
        for b in b1, b2:

