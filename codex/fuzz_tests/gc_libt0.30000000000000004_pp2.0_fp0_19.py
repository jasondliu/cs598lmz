import gc, weakref

import numpy as np

import pytest

from pynwb.core import NWBDataInterface, NWBDataRegion
from pynwb.file import NWBFile
from pynwb.form.backends.hdf5 import HDF5IO
from pynwb.form.backends.hdf5.h5_utils import H5DataIO
from pynwb.testing import create_fake_h5_file, TestCase


class TestHDF5IO(TestCase):

    def test_create_and_read_file(self):
        """
        Test that we can create a file and read it back in.
        """
        h5_file = create_fake_h5_file()
        with HDF5IO(h5_file, 'r') as io:
            nwbfile = io.read()
            assert isinstance(nwbfile, NWBFile)

    def test_write_and_read_file(self):
        """
        Test that we can create a file and read it back in.
        """
        h5_file = create_
