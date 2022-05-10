import codecs
# Test codecs.register_error('my_error', codecs.replace_errors)

def test_decode_error(self):
    self.assertEqual(b"abc\xff".decode('ascii', 'my_error'),
                     u"abc\ufffd")
