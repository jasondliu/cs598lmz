from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'add1')(1))

# ==============================================================================
# Enumerator objects
# ==============================================================================
from itertools import count
def sequence(start=0, step=1):
    return map(lambda i: start + i * step, count())

# ==============================================================================
# Itertools
# ==============================================================================
#
# Itertools is a powerful module for creating iterators for efficient looping.
#
# You can see all the available methods for iterators using:
from itertools import *
from pprint import pprint
pprint(dir(itertools))

# ==============================================================================
# Accumulate
# ==============================================================================
list(accumulate(range(10)))
from operator import mul
list(accumulate(range(1, 11), mul))

# ==============================================================================
# Chain
# ==============================================================================
list(chain('ABC', range(2)))

# ==============================================================================
# Compress
# ==============================================================================
list(compress('ABCDF', [1, 0, 1, 0, 1]))

# =================================================================
