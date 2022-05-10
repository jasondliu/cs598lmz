import gc, weakref
import numpy as np

from numpy.testing import assert_array_equal, assert_array_almost_equal
from nose.tools import assert_true, assert_false, assert_equal, assert_raises

import mne


def test_io_raw():
    """Test IO for raw data (fif + brainvision + gdf)"""
    tempdir = _TempDir()
    raw_fname = op.join(tempdir, 'test_raw.fif')
    raw_ctf_fname = op.join(tempdir, 'test_ctf_raw.fif')
    raw_gdf_fname = op.join(tempdir, 'test_raw.gdf')
    raw_bv_fname = op.join(tempdir, 'test_raw.vhdr')
    event_name = op.join(tempdir, 'test-eve.fif')

    # Set up pick list: MEG + STI 014 - bad channels
    include = ['STI 014']
    raw = mne.fiff.Raw(raw_fname, pre
