import lzma
# Test LZMADecompressor, and also test that LZMAError is raised
# when an attempt is made to decompress more than the maximum amount
# of input data (2 GiB).
data_1GiB = b'a' * 2**30
if lzma.FORMAT_RAW in lzma.check_format(data_1GiB):
    test.test_suite.load_tests_from_module(sys.modules[__name__])
else:
    sys.stderr.write('Test skipped: {0} not in lzma.check_format()\n'.format(
        repr(data_1GiB)))
