import threading
threading._DummyThread._Thread__stop = lambda x: 42
            
import time
import sys
import pathlib
import numpy as np
import h5py
import json
import traceback

import slycat.hdf5
import slycat.email
import slycat.web.server
import slycat.web.client

def parse_inputs(argv):
    parser = optparse.OptionParser()
    parser.add_option("--host", default="localhost",
                      help="Server hostname.  Use localhost for a server on the same machine.")
    parser.add_option("-p", "--port", default=8088,
                      help="Server port.  Use 8088 for a server on the same machine.")
    parser.add_option("--input", default="input.hdf5",
                      help="HDF5 file containing the input data.  Defaults to %default.")
    parser.add_option("--output", default="output.hdf5",
                      help="HDF5 file containing the output data.  Defaults to %default.")
