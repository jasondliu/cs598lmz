import gc, weakref
import numpy as np

from util import profilable

# Import functions from module stream
from stream import get_window, plot_window
from stream import plot_intensity
from stream import _is_md, _stream_types

from stream import MDAccumulator, MDStream
from stream import XYSAccumulator, XYStream
from stream import EventAccumulator, EventStream

from stream import plot_saxs

class ImageProcessor(GenericProcessor):
    _META_FIELDS = ['time_spent', 'proctype', 'procid', 
                    'beamcenter_x', 'beamcenter_y', 
                    'wavelength']

    @classmethod
    def auto_configure(cls, proc_id):
        self = cls(proc_id=proc_id)
        return self.configure()

    def configure(self, force=False):
        """Configuration steps."""

        ## Image size ##
        # row and column indices reference the beam center
        self.i_ref = 0
        self.j_ref = 0

       
