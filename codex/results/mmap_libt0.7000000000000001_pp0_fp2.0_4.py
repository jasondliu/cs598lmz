import mmap

import numpy as np
from collections import Iterable
from numpy import genfromtxt

from . import _update_path
from . import _check_fname
from . import check_numpy_version
from .fixes import in1d, unique


def _read_segments_file(fname, tree=None, node_indices=None, verbose=None):
    """Read events from a text file.

    Parameters
    ----------
    fname : str
        Name of the text file.
    tree : list
        List of strings for the path to the channels. If None, all events
        are returned.
    node_indices : list | None
        If not None, only load the events for the given node indices.
    verbose : bool, str, int, or None
        If not None, override default verbose level (see mne.verbose).

    Returns
    -------
    segs : list of arrays
        The events.
    """
    check_fname(fname, verbose=verbose, must_exist=True)
    segs = []
