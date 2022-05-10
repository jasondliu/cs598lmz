import _struct
import struct
import argparse
import sys
import os

from itertools import islice
from six.moves import range # pylint: disable=redefined-builtin
import yaml
import logging
from . import proto  # pylint: disable=relative-import
from dfi_utils.processlist import ProcessList

logger = logging.getLogger('dfi.pe')

if sys.version_info[0] == 3:
    _struct_pack = _struct.Struct('<I').pack
    _struct_unpack = _struct.Struct('<I').unpack
    _xrange = range

    def _foreach_range(l, n=2):
        """Yield successive n-sized chunks from l."""
        it = iter(l)
        while True:
            try:
                x = [next(it) for _ in _xrange(n)]
            except StopIteration:
                break
            yield x
else:
    _struct_pack = _struct.Struct('<I').pack
    _struct_unpack = _
