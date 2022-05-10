import codecs
codecs.register_error('strict', codecs.ignore_errors)

if sys.version_info >= (3,0):
    def u(x):
        return x
else:
    def u(x):
        return x.decode("utf-8")

class TestMisc(unittest.TestCase):
    def test_unicode_file_read(self):
        # This is a regression test for issue #8
        # https://github.com/moliware/tesseract.py/issues/8
        f = open("tests/test.tif", 'rb')
        image = Image.open(f)
        f.close()
        tesseract.image_to_string(image)

class TestTesseract(unittest.TestCase):
    def setUp(self):
        self.api = tesseract.TessBaseAPI()
        r = self.api.Init(".", "eng", tesseract.OEM_DEFAULT)
        self.assertEqual(r, tesseract.SUCCESS)

    def tearDown
