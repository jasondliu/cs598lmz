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
