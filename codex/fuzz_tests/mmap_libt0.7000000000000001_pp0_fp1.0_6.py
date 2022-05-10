import mmap
import mmap_range
import numpy as np
from PIL import Image

import pyximport
pyximport.install(setup_args={'include_dirs':[np.get_include()]})
from mmap_range_array import mmap_range_array

"""
This module includes functions to interact with memory-mapped image data.
"""

def get_mmap_image_data(fname, dtype='uint8'):
    """Get a memory-mapped array of the pixel data from an image file.
    
    Args:
        fname: The path to an image file.
        
    Returns:
        A memory-mapped array for the pixel data.
    """
    return mmap_range_array(mmap.mmap(fname, 0), dtype)

def get_image_data(fname, dtype='uint8'):
    """Get the pixel data from an image file as a numpy array.
    
    Args:
        fname: The path to an image file.
        
    Returns:
        The
