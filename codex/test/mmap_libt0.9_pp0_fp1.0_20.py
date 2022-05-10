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
