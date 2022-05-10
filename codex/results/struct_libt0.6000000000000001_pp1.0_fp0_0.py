import _struct
import struct
import sys

from .. import _util
from .. import abnf
from .. import error
from .. import h2
from .. import hpack
from .. import http2
from .. import http_common
from .. import http_headers
from .. import huffman
from .. import tls

from . import h2_frame

# Python 3.4 doesn't have math.isfinite, so we need to provide a replacement.
try:
  from math import isfinite
except ImportError:
  def isfinite(x):
    return x == x and x != float('inf') and x != -float('inf')

# Python 3.4 doesn't have math.isnan.
try:
  from math import isnan
except ImportError:
  def isnan(x):
    return x != x

_logger = _util.get_logger()


# Do not use these constants directly.
# Use the functions defined in this module instead.
H2ConnectionState = h2_frame.H2ConnectionState
H2StreamState = h2_frame.H2
