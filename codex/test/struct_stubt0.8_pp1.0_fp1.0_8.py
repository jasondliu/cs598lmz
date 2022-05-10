from _struct import Struct
s = Struct.__new__(Struct)
def __(format, self=s, *args):
    self.format = format
    self.size = self.sizeof()
    return self.pack(*args)
s.__call__ = __
__(
    'B'              # frame_type
    'L'              # frame_size
    'L'              # application_size
    'L'              # application_offset
    'B'              # OS_version_size
    'B'              # OS_version_offset
    'B'              # application_version_size
    'B'              # application_version_offset
    'L'              # vendor_size
    'L'              # vendor_offset
    'L'              # timestamp
    'H'              # runtime_size
    'H'              # runtime_offset
)

class MSCFTag(object):
    '''
    Microsoft Compound File Type

    tag:     7 bytes.
    '''
    __slots__ = 'tag'

    def __init__(self, tag):
        self.tag = tag
