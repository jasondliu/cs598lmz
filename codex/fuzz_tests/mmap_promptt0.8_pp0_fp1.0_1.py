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

# Test availability of some optional C headers
optional_headers = ['assert.h', 'complex.h', 'dlfcn.h', 'fenv.h', 'fpu_control.h',
                    'ieeefp.h', 'inttypes.h', 'iso646.h', 'limits.h', 'locale.h',
                    'setjmp.h', 'signal.h', 'stdarg.h', 'stdbool.h', 'stddef.h',
                    'stdint.h', 'stdio.h', 'stdlib.h', 'string.h', '
