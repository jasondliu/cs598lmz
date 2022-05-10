import bz2
# Test BZ2Decompressor() and BZ2Compressor() before passing as argument to
# CompressedFile
try:
    bz2.BZ2Decompressor().decompress(b"")
    bz2.BZ2Compressor().compress(b"")
except Exception:
    bz2 = None

from pyfakefs.extra_packages.mock import MagicMock
import pytest

from pyfakefs.tests.utils import patch_open, assert_fs_equal, assert_fs_contents
from pyfakefs.tests import skip_if_windows, skip_if_not_bz2


@skip_if_not_bz2
class BZ2CompressedFileTest(CompressedFileTest):
    """Test bzip2 compressed files."""

    def _compress_func(self):
        return bz2.compress

    def _decompress_func(self):
        return bz2.decompress

    def _process_file(self, testfile, mode):
        return bz2.BZ2File(testfile, mode)

    @
