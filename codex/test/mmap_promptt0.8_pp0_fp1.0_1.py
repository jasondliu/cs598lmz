import mmap
# Test mmap.mmap exists and is callable
if mmap.hasattr(mmap, 'mmap') and callable(mmap.mmap):
    mmap_avail = True
else:
    mmap_avail = False

import numpy
import numpy.distutils.misc_util

# make sure we can import docutils -- is not a build requirement,
# but needed by some other modules.
try:
    import docutils.examples
except ImportError:
    docutils = None

