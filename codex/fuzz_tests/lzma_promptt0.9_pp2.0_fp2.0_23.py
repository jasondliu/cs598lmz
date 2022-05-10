import lzma
# Test LZMADecompressor.readinto() with files with headers and indexes.
# Padded files don't work right; the LZMA library pads the output to the
# next multiple-of-four bytes.  That may be a bug, or it may be intentional.
TEST_FILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_files')
if TEST_FILES_DIR:
    UNPADDED_LZMA_FILES = os.path.join(TEST_FILES_DIR, 'lzma-files')
    PADDED_LZMA_FILES = os.path.join(TEST_FILES_DIR, 'lzma-files-padded')
    TEST_FILES = [unpadded_lzma_files,  PADDED_LZMA_FILES]

def _lzma_index_is_valid(index, orig_size):
    """Check that index is a valid LZMA index

    Tests that the specified index is a valid LZMA index and has the expected

