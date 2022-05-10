import lzma
# Test LZMADecompressor to find out if lzma is available
try:
    lzma.LZMADecompressor()
    lzma_available = True
except NameError:
    lzma_available = False


class TestArchiveReader(unittest.TestCase):
    """Test ArchiveReader"""

    # noinspection PyMissingOrEmptyDocstring,PyMissingTypeHints
    def test_read_tar(self):
        # type: () -> None
        # test reading a tar file
        for format in ["tar", "tar.gz", "tar.bz2"]:
            with ArchiveReader(TAR_FILE, format) as tarfile:
                tar_content = tarfile.read()
            self.assertIsInstance(tar_content, bytes)
            self.assertIn(b"file", tar_content)

    # noinspection PyMissingOrEmptyDocstring,PyMissingTypeHints
    def test_read_zip(self):
        # type: () -> None
        # test reading a zip file
        with ArchiveReader(ZIP_FILE, "zip") as zipfile
