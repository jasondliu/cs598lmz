import _struct
from _testcapi import ISNAN, INFINITY

import warnings
warnings.filterwarnings("ignore")

# --- data input API

def parser(path):
    """
    Raw Memory data parser

    Parameters
    ----------
    path : str
        The path of the data file.
        The extension should be ".xyz".

    Returns
    -------
    meta : dict
        The meta data.
    data : list[dict]
        The data.
    """
    
    meta = {"path": path}

    with open(path, "rb") as f:
        head_size = 8
        head_raw = f.read(head_size)
        valid_head = (head_raw[0] == 0x4C) and (head_raw[1] == 0x4C) and (head_raw[2] == 0x4D)
        assert valid_head

        data_size = _struct.unpack("<I", head_raw[4:])[0] + 8 # note: type(data_size) -> int, not long

