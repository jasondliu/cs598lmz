import mmap
# Test mmap.mmap.__doc__
from mmap import mmap
assert mmap.__doc__ == 'mmap(fileno, length[, flags[, prot[, access[, offset]]]]) -> mmap'

from mmap import ACCESS_READ
from mmap import ACCESS_WRITE
from mmap import MAP_ANON
from mmap import MAP_SHARED
from mmap import MAP_PRIVATE
from mmap import PROT_EXEC
from mmap import PROT_READ
from mmap import PROT_WRITE
from mmap import PROT_NONE
from mmap import ALLOCATIONGRANULARITY

from mmap import error
from mmap import MADV_DONTNEED
from mmap import MADV_NORMAL
from mmap import MADV_RANDOM
from mmap import MADV_SEQUENTIAL
from mmap import MADV_WILLNEED

from mmap import MAP_FAILED

from mmap import _mmap
from mmap import _ACCESS_DEFAULT
from mmap import _ACCESS_COPY
