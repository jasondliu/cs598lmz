from _struct import Struct
s = Struct.__new__(Struct)
# End of Structure definitions.

#------------------------------------------------------------------------------

class LPC(object):
    """
    A class representing a LPC record.
    """
    def __init__(self,lpc=None,parent=None):
        self.data = lpc
        self.parent = parent
        self.lpc = lpc

    @property
    def sibling(self):
        return self._sibling

    @sibling.setter
    def sibling(self,value):
        self._sibling = value

    @property
    def path(self):
        return _get_path(self)

    @property
    def name(self):
        return self.lpc.m_Name

    @property
    def size(self):
        """
        Size of the LPC record in bytes.
        """
        return sizeof(self.lpc)

    @property
    def pos(self):
        return self.parent.lpc_pos(self)

    @property
    def subrecords(self):
        """
        Yields subrecords.
        """
