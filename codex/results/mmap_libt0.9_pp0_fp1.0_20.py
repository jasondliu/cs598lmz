import mmap
import numpy as np
import struct
import os
import re

class FloatAdapter:
    """This store is a convenient interface for accessing data in
    files. An instance of this class creates a memory map over a file
    that contains data of single precision floats. The memory map gets
    initialized with data and methods are provided to read and write
    slices.
    """
    def __init__(self, path, shape=None, dtype=None):
        """Creates an instance of the file store.

        Initializes the memory map by loading data from the file
        stored at path. The shape of the data can either be passed as
        an argument if known or has to be given in the file's name
        (see format of file name below).

        Args:
          path: The path to the data file.
          shape: The shape of the data stored in the file (if known).
          dtype: The data type of the data stored in the file (if
            known).

        When neither the shape nor the type is given, then the data
        file name has to give the shape and type of the data.
