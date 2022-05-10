import _struct

#===============================================================================
# 
#===============================================================================

class _struct_unpack(object):
    """
    This class is used to unpack a binary data stream into a Python object.
    """
    def __init__(self, format, data):
        self.format = format
        self.data = data
        self.size = _struct.calcsize(self.format)
        self.offset = 0
        self.endian = '<'
        
    def unpack(self):
        """
        Unpack the data and return the result.
        """
        if self.offset + self.size > len(self.data):
            raise ValueError('Not enough data to unpack')
        
        result = _struct.unpack(self.endian + self.format, self.data[self.offset:self.offset + self.size])
        self.offset += self.size
        return result
    
    def unpack_string(self):
        """
        Unpack a string.
        """
        length = self.unpack()[0]

