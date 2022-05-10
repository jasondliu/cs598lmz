import _struct

#
#  C O N S T A N T S
#

#
#  P R I V A T E   D A T A
#

#
#  P U B L I C   F U N C T I O N S
#

#
#  P R I V A T E   F U N C T I O N S
#

#
#  C L A S S E S
#

class _Struct(object):
    def __init__(self, format):
        self.format = format
        self.size = _struct.calcsize(format)

    def pack(self, *args):
        return _struct.pack(self.format, *args)

    def unpack(self, data):
        return _struct.unpack(self.format, data)

class _Struct2(object):
    def __init__(self, format, size):
        self.format = format
        self.size = size

    def pack(self, *args):
        return _struct.pack(self.format, *args)

   
