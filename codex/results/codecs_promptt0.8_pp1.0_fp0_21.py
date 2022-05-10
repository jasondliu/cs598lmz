import codecs
# Test codecs.register_error
class Test_register_error(unittest.TestCase):
    def test_register_error(self):
        s = b'\xff'
        def replace_ff(exc):
            if not isinstance(exc, UnicodeDecodeError):
                raise TypeError("don't know how to handle %r" % exc)
            x = []
            for c in exc.object[exc.start:exc.end]:
                x.append('%%%02X' % c)
            return (''.join(x), exc.end)
        old_handler = codecs.register_error('replace_ff', replace_ff)
        self.assertIs(old_handler, None)
        self.assertEqual(codecs.decode(s, 'latin-1', 'replace'), '%FF')
        self.assertEqual(codecs.decode(s, 'latin-1', 'replace_ff'), '%FF')
        self.assertEqual(codecs.encode(s, 'latin-1', 'strict'), b'\xff')
       
