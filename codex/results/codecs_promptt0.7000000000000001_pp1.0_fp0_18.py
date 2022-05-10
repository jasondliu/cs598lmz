import codecs
# Test codecs.register_error()
def bad_decode(input, errors='strict'):
    raise TypeError("bad_decode")
codecs.register_error('test.bad_decode', bad_decode)
with self.assertRaises(TypeError) as cm:
    s = b'\xff'.decode('ascii', 'test.bad_decode')
self.assertEqual(str(cm.exception), 'bad_decode')
# Test codecs.register_error()
def bad_encode(input, errors='strict'):
    raise TypeError("bad_encode")
codecs.register_error('test.bad_encode', bad_encode)
with self.assertRaises(TypeError) as cm:
    u = '\u2603'.encode('ascii', 'test.bad_encode')
self.assertEqual(str(cm.exception), 'bad_encode')
# Test codecs.register_error()
def bad_encode(input, errors='strict'):
    raise TypeError("bad_
