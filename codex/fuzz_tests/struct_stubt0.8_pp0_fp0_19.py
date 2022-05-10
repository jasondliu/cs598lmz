from _struct import Struct
s = Struct.__new__(Struct)
s.format = "i"
s.size = 4
s.mcs = mcs
s
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(mcs.recv(4))
s.unpack(m
