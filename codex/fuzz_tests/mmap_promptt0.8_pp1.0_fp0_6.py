import mmap
# Test mmap.mmap file object
from io import BytesIO
from backports.tempfile import TemporaryDirectory
import pickle

from pytest import raises
from nose.tools import assert_raises_regex
from unittest import mock

from numpy import arange, array, ndarray
from numpy.testing import assert_array_equal, assert_array_almost_equal

from thunder.rdds.fileio.readers import _open_file
from thunder.rdds.fileio.readers import frombinary, fromimages, fromtifffile
from thunder.rdds.fileio.writers import tobinary, toimages, Totifffile, fromarrays, fromarraysindices
from thunder.utils.common import check_mode_valid, check_large
from thunder.utils.datasets import DataSets


class TestUtilFunctions(unittest.TestCase):
    def test_check_large(self):
        with raises(Exception) as e:
            check_large('large', 'small', 'large')
        assert e.value.args[0] == 'large must be greater
