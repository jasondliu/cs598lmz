import codecs
codecs.register_error('surrogate_or_special', surrogatepass)

# The following is from lib/python/test/test_io.py by Benjamin Peterson.
class TestIO(object):
    def test_encodings(self):
        for enc in ['ascii', 'latin-1', 'utf-8']:
            # check encoding/decoding of single character strings
            for i in xrange(256):
                s = chr(i)
                t = s.decode(enc)
                if i == 0 or (32 <= i <= 126):
                    self.assertEqual(t, s)
                else:
                    self.assertEqual(t, '\\x%02x' % i)
                self.assertEquals(s.encode(enc), t.encode(enc))
                # check decoding of raw bytes
                self.assertEquals(s.encode(enc), chr(i).decode(enc).encode(enc))

            # test surrogate pass error handler
            self.assertEquals(u'\ud800'.encode('utf-8', '
