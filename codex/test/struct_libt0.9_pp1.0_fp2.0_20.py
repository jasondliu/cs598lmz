import _struct

try:
    import cStringIO as StringIO
except:
    import StringIO

base_types = {
    1: 'byte',
    2: 'short',
    3: 'int',
    4: 'float',
    5: 'string',
    6: 'string',
    7: 'data',
    8: 'int',
    9: 'long',
    10: 'int',
    11: 'int',
    12: 'int',
    13: 'int',
}

data_types = {
    0: 'vector3',
    1: 'string',
    2: 'string_prime',
    3: 'byte_array',
    4: 'int_array',
    7: 'vector2',
    8: 'vector3',
}

class Data(object):

    def __init__(self, reader):
        self.position = 0
        self.size = reader.size
        self.reader = reader
        self.base_type = None
        self.data_type = None

