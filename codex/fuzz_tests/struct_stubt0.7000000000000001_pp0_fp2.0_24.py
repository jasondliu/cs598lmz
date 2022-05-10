from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<HI')  # set format
s.size  # size of record

data = buffer('Hello World')  # make buffer from string
s.unpack_from(data, 0)  # unpack first record in data
