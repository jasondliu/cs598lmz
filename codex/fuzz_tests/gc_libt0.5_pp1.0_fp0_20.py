import gc, weakref
import numpy as np

from mpi4py import MPI

from dedalus.tools.config import config
from dedalus.tools.logger import logger
from dedalus.tools.parallel import Sync, Barrier

# MPI constants
MPI_TAG_ANY = MPI.ANY_TAG
MPI_ANY_SOURCE = MPI.ANY_SOURCE

# MPI command tags
CMD_STOP = 0
CMD_START = 1
CMD_PAUSE = 2
CMD_STEP = 3
CMD_CONTINUE = 4

# MPI status tags
STAT_OK = 0
STAT_ERROR = 1

# MPI data tags
DATA_SEND = 0
DATA_RECV = 1
DATA_SEND_RECV = 2

# Default MPI buffer size
BUFFER_SIZE = config['mpi']['buffer_size']


class MPI_exception(Exception):
    pass


class MPI_parent(object):
    """Parent class for MPI-parallelized objects."""

    def __init__(self,
