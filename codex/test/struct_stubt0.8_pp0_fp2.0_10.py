from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I'
for i in xrange(64):
    try:
        s.size = i
    except ValueError as e:
        print(e)
        break
