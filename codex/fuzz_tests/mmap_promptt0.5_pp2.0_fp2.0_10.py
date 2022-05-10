import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

import numpy as np

from . import util
from . import constants as const
from . import config
from . import alignment
from . import signal

from .alignment import align_by_index
from .alignment import align_by_sequence
from .alignment import align_by_clustal
from .alignment import align_by_muscle
from .alignment import align_by_mafft
from .alignment import align_by_prank
from .alignment import align_by_probalign

from .signal import find_signals
from .signal import find_signals_scipy
from .signal import find_signals_numpy
from .signal import find_signals_numba
from .signal import find_signals_numba_parallel
from .signal import find_signals_numba_parallel2
from .signal import find_signals_numba_parallel3
from .signal import find_signals_n
