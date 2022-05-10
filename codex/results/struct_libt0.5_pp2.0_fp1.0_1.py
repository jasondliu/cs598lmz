import _struct
from _testcapi import INT_MAX, INT_MIN, UINT_MAX, ULONG_MAX

from collections import namedtuple
from struct import error
from test import support
from test.support import bigmemtest, bigaddrspacetest

# The struct module is not supported on all platforms. Skip these tests
# on those that don't have it.
support.import_module('struct')

try:
    from _testcapi import getargs_b, getargs_B, getargs_h, getargs_H, \
        getargs_i, getargs_I, getargs_l, getargs_k, getargs_L, getargs_n, \
        getargs_N, getargs_q, getargs_Q, getargs_e, getargs_f, getargs_d, \
        getargs_s, getargs_p, getargs_P
except ImportError:
    raise unittest.SkipTest("test needs _testcapi")


# These are used in the byte order tests below.
_big_endian = (sys.byteorder ==
