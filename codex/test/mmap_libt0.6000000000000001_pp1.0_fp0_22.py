import mmap
import os
import re
import sys

if sys.version_info[0] == 2:
    from StringIO import StringIO
else:
    from io import StringIO

import numpy as np

from .._extern.six import reraise

from .. import units as u
from ..extern.six.moves import xrange

from . import _read
from . import _write
from . import conf
from . import _connect


__all__ = ['FITS', 'connect', 'HDUList', 'PrimaryHDU', 'ImageHDU', 'BinTableHDU',
           'TableHDU', 'new_table', 'ConvenienceHDU', 'GroupData',
           'GroupsHDU', 'Undefined', 'open', 'ColDefs', 'Column', 'BinTableHDU',
           'FITS_rec', 'FITS_record', 'table_to_hdu', 'table_to_fits',
           'append']


