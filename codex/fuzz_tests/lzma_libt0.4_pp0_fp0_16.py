import lzma
lzma.LZMA_FILTER_X86

#
# 
#
#
#

class LzmaFilter(object):
    def __init__(self, id, props):
        self.id = id
        self.props = props
        self.name = "LZMA Filter"
        self.desc = "LZMA Filter"
        self.filter = lzma.LZMAFilter(id, props)
        self.out_size = None
        self.out_pos = 0
        self.out_buf = bytearray()

    def __repr__(self):
        return "LzmaFilter(id=%d, props=%s)" % (self.id, repr(self.props))

    def reset(self):
        self.out_size = None
        self.out_pos = 0
        self.out_buf = bytearray()
        self.filter.reset()

    def set_props(self, props):
        self.props = props
        self.filter.set_props(pro
