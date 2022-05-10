import _struct
# Test _struct.Struct formats against struct.Struct

from support import TestSkipped

import sys

# In case we're running with -A we don't want warnings
import warnings
warnings.simplefilter('ignore')

# Modules under test:
mod = _struct

# Pre-calculated results
format_size = {
    'x': 1,
    'c': 1,
    'b': 1,
    'B': 1,
    '?': 1,
    'h': 2,
    'H': 2,
    'i': 4,
    'I': 4,
    'l': 4,
    'L': 4,
    # In Pristine source the stg added for the next format code e.g float 'f'
    # is 4, so the pair is too big for 'l' packing and causes SkipTest.
    # f'i{number} throws ZeroDivisionError: n must be nonzero already, so
    # crashes.
    'f': 4,
    #'f': getattr(_struct, 'calcsize', struct.calcsize)('l'),

