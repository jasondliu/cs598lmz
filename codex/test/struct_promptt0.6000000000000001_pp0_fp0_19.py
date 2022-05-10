import _struct
# Test _struct.Struct.

from test import support

import struct
import sys

# On platforms with native alignment restrictions, pack_into() and
# pack_into_from() must raise an exception if the item to be packed is not
# aligned.

if support.check_impl_detail(pypy=False):
    def test_pack_into_from_align(self):
        # Issue #12084: pack_into() and pack_into_from() must raise an
        # exception if the item to be packed is not aligned.
        s = _struct.Struct('i')
        buf = bytearray(s.size + 1)
        # pack_into()
        with self.assertRaises(struct.error):
            s.pack_into(buf, 1, 1)
        # pack_into_from()
        with self.assertRaises(struct.error):
            s.pack_into_from(buf, 1, 1, 0)

# Issue #7207: Allows to specify alignment in _struct.Struct.

