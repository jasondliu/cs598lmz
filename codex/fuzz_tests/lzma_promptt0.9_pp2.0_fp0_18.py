import lzma
# Test LZMADecompressor
VALID_MULTIPLE = (lambda comp: comp._unconsumed_tail != b'')
INVALID_MULTIPLE = (lambda comp: comp._buffer.getvalue() != b'')
INVALID_SINGLE = (lambda comp: comp.unused_data != b'')
Test.add_unittest(unittest.defaultTestLoader.loadTestsFromTestCase(
            LZMADecompressorTests))
Test.add_unittest(unittest.defaultTestLoader.loadTestsFromTestCase(
            LZMADecompressorTestsWithoutBits))
Test.add_unittest(unittest.defaultTestLoader.loadTestsFromTestCase(
            LZMADecompressorMultipleUnconsumedErrorTests, validator=VALID_MULTIPLE))
Test.add_unittest(unittest.defaultTestLoader.loadTestsFromTestCase(
            LZMADecompressorUnusedDataErrorTests, validator=(INVALID_SINGLE, INVALID_MULT
