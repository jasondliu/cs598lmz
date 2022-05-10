import codecs
# Test codecs.register_error.
# Issue 7899
results = b'\x7f'
for codec in ('utf_8', 'ascii'):
    for error in ('strict', 'ignore', 'replace', 'surrogateescape'):
        with codecs.open(TESTFN, 'w', codec, errors=error) as f:
            f.write(b'abcd\x7fef')
        with codecs.open(TESTFN, 'r', codec, errors=error) as f:
            if error == 'strict':
                self.assertRaises(UnicodeDecodeError, f.read)
            else:
                if error == 'replace':
                    results = 'abcd\ufffdef'
                elif error == 'ignore':
                    results = 'abcdef'
                elif error == 'surrogateescape':
                    results = 'abcd\udc7fef'
                self.assertEqual(f.read(), results)
        os.unlink(TESTFN)


class BerkeleyDBTest(unittest.TestCase):
    """For
