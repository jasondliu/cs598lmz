import types
types.ModuleType.__repr__ = types.ModuleType.__str__

from . import io
from . import tools
from . import version
from . import __version__

class FITSFile(io.FITSFile):
    def __init__(self, *args):
        super(FITSFile, self).__init__(*args)
        self.__repr__ = self.__str__


class FITS(object):
    """
    A simple FITS file wrapper.

    """
    def __init__(self, *args, **kwargs):
        """
        Reads a FITS file.

        Parameters
        ----------
        filename : str
            Name of the file to read.
        memmap : bool
            Whether to use a memory map to load the file.
        mode : str
            File mode for the FITS file.

        """
        self.filename = args[0]
        self.memmap = kwargs.get('memmap', True)
        self.mode = kwargs.get('mode', 'readonly')

        self._file =
