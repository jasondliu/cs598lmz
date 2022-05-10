import lzma
lzma.LZMAError('test')

try:
    import pylzma
    pylzma.LZMAError('test')
except ImportError:
    pass

class Lzmamod_test(testutil.CliTestCase):
    def setUp(self):
        super(Lzmamod_test, self).setUp()
        self.files = ['test1.txt', 'test2.txt', 'test3.txt']
        testutil.create_files(self.files)
        self.path = os.getcwd()

    def tearDown(self):
        for f in self.files:
            os.remove(f)
        super(Lzmamod_test, self).tearDown()

    def test_main(self):
        data = ' '.join(self.files)
        testutil.call('lzmamod', '-z', data)
        testutil.call('lzmamod', '-d', data=data)
        testutil.call('lzmamod', '-t
