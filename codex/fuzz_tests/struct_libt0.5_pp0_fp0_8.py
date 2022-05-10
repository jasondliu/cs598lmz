import _struct

from . import struct
from . import util
from . import block
from . import data
from . import field
from . import type
from . import value

#------------------------------------------------------------------------------
# Struct
#------------------------------------------------------------------------------

class Struct(block.Block):
    """
    A struct.
    """

    _cached_fields = None
    _cached_fields_dict = None

    def __init__(self, *args, **kwargs):
        super(Struct, self).__init__(*args, **kwargs)
        self._cached_fields = None
        self._cached_fields_dict = None

    #--------------------------------------------------------------------------
    # Properties
    #--------------------------------------------------------------------------

    @property
    def is_struct(self):
        return True

    @property
    def fields(self):
        """
        A list of fields contained in the struct.
        """
        if self._cached_fields is None:
            self._cached_fields = self._get_fields()
        return self._cached_fields

    @property
    def fields_dict(self):
        """
