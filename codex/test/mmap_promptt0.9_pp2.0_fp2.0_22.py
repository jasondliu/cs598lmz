import mmap
# Test mmap.mmap.__init__
from mmap import mmap
from mmap import ALLOCATIONGRANULARITY
import shutil

from lib import support

# Lists of supported file types.
# Should test writing in text and binary mode?  What about the others?
types_32 = [(mmap.ALLOCATIONGRANULARITY, 16 * mmap.ALLOCATIONGRANULARITY)]
types_64 = [(mmap.ALLOCATIONGRANULARITY, 16 * mmap.ALLOCATIONGRANULARITY),
            (16 * mmap.ALLOCATIONGRANULARITY, 20 * mmap.ALLOCATIONGRANULARITY)] # Bug 684110
types = types_32 + types_64

# Resource warning is silenced because mmap.close triggers one during 3.2-3.7.
support.suppress_resource_warning(mmap)
support.unlink(support.TESTFN)

# Create a bunch of random files for use in the tests.
filenames = []
for type in types:
    filename = support.TESTFN + str(type)
    f
