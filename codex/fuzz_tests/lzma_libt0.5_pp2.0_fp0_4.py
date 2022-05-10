import lzma
lzma.LZMAFile

import numpy as np

from . import raster
from . import vector

__all__ = ['RasterFile', 'VectorFile', 'GeoFile']


class GeoFile:
    """
    GeoFile class for reading and writing geospatial files.

    Attributes
    ----------
    filename : str
        Filename of the file.
    file_type : str
        Type of the file.
    compression : str
        Compression method used.
    compression_level : int
        Compression level used.
    """

    def __init__(self, filename, file_type=None, compression='gzip',
                 compression_level=6):
        """
        Initialize GeoFile instance.

        Parameters
        ----------
        filename : str
            Filename of the file.
        file_type : str
            Type of the file.
        compression : str
            Compression method used.
        compression_level : int
            Compression level used.
        """

        self.filename = filename
        self.file_type = file_type
       
