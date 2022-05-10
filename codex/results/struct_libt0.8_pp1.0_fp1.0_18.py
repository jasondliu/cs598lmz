import _struct
from .flags import *
from .munge import munge
from .util import *

class CffFont(object):
    """The base class to read CFF font data.
    """

    def __init__(self, file):
        self.file = file
        self.cff = read_cff_font(self.file)

    def dump(self):
        """Dump all data.
        """
        return self.cff.dump()

    def get_data(self, index_name):
        """Get binary data specified by the index_name.
        """
        return get_data(self.cff, index_name)

    def get_fontinfo_data(self):
        """Get the fontinfo data.
        """
        return get_fontinfo_data(self.cff)

    def get_name(self):
        """Get the font name.
        """
        return get_name(self.cff)

    def charstrings_by_gnames(self):
        """Get a dictionary of charstrings keyed by global subroutin
