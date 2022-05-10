import codecs
# Test codecs.register_error('strict', strict_errors)
# Test codecs.register_error('ignore', ignore_errors)
# Test codecs.register_error('replace', replace_errors)

import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    from test import support


class Test_StreamWriter(unittest.TestCase):
    def test_streamwriter(self):
        # Issue #10791: test that StreamWriter.write() returns the number of
        # characters written
        f = io.BytesIO()
        self.assertEqual(f.write(b'\xe9'), 1)
        f.seek(0)
        writer = codecs.getwriter('latin-1')(f)
        self.assertEqual(writer.write('\xe9'), 1)
        self.assertEqual(writer.write('abc'), 3)
        self.assertEqual(writer.write('def'), 3)


class Test_StreamReader(unittest.TestCase):
    def test_streamreader(self
