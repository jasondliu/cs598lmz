from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'IHH'

data = open(sys.argv[1]).read()

