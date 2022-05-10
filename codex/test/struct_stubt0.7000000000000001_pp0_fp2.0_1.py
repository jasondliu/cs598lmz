from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

import _pickle
p = _pickle.Pickler.__new__(_pickle.Pickler)
p.__init__(None)
p.dump(s)

data = p.memo

#print(data)

#data = b'\x80\x03c_struct\nStruct\nq\x00)\x81q\x01X\x03\x00\x00\x00>iq\x02\x86q\x03Rq\x04.'

p = _pickle.Pickler.__new__(_pickle.Pickler)
p.__init__(None)

s = p.load()

s.size
