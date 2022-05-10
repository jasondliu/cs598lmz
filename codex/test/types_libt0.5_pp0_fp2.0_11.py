import types
types.SimpleNamespace()

import json
import os
import sys

from ctypes import *

from mpi4py import MPI

from ezrcluster.util import logger as log
from ezrcluster.util import mpi as mpi_utils
from ezrcluster.util import utils

from ezrcluster.master import Master
from ezrcluster.worker import Worker

#------------------------------------------------------------------------------

def main():
    # Get MPI communicator.
    comm = MPI.COMM_WORLD

    # Get MPI rank and size.
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Get the hostname of this process.
    hostname = MPI.Get_processor_name()

    # Get the cluster configuration.
    config = utils.get_config()

    # Get the cluster name.
    cluster_name = config['cluster']['name']

    # If this is the master process, start the master process.
